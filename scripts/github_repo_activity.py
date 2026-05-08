#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import re
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def parse_repos(path):
    repos = []
    pat = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith('#') or s.startswith('```'):
                continue
            s = s.strip('`')
            if pat.match(s):
                repos.append(s)
    return repos


def gh_get(url, token=None):
    req = Request(url)
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('User-Agent', 'plan-github-activity-monitor')
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))


def classify(count_30d):
    if count_30d >= 20:
        return 'daily'
    if count_30d >= 4:
        return 'weekly'
    if count_30d >= 1:
        return 'monthly'
    return 'stale'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--window-days', type=int, default=30)
    ap.add_argument('--output-md', required=True)
    ap.add_argument('--output-json', required=True)
    args = ap.parse_args()

    token = os.getenv('GITHUB_TOKEN')
    repos = parse_repos(args.input)
    now = dt.datetime.utcnow().replace(microsecond=0)
    since = now - dt.timedelta(days=args.window_days)

    rows = []
    for repo in repos:
        try:
            # last commit
            c_url = f'https://api.github.com/repos/{repo}/commits?per_page=1'
            c = gh_get(c_url, token=token)
            if isinstance(c, dict) and c.get('message'):
                raise RuntimeError(c.get('message'))
            last = c[0]
            last_sha = last.get('sha', '')[:8]
            commit_obj = last.get('commit', {})
            author_obj = commit_obj.get('author', {})
            last_date = author_obj.get('date')
            last_author = author_obj.get('name', '')

            # count commits in window (cheap: paginate until older than since)
            page = 1
            total = 0
            done = False
            capped = False
            while not done and page <= 10:  # hard cap to avoid abuse
                q = urlencode({'since': since.isoformat() + 'Z', 'per_page': 100, 'page': page})
                u = f'https://api.github.com/repos/{repo}/commits?{q}'
                batch = gh_get(u, token=token)
                if isinstance(batch, dict) and batch.get('message'):
                    raise RuntimeError(batch.get('message'))
                n = len(batch)
                total += n
                if n < 100:
                    done = True
                page += 1
            if not done:
                capped = True

            state = classify(total)
            rows.append({
                'repo': repo,
                'last_commit_date': last_date,
                'last_commit_sha': last_sha,
                'last_commit_author': last_author,
                'commits_window': total,
                'window_days': args.window_days,
                'activity': state,
                'count_capped': capped,
                'error': None,
            })
        except Exception as e:
            rows.append({
                'repo': repo,
                'last_commit_date': None,
                'last_commit_sha': None,
                'last_commit_author': None,
                'commits_window': None,
                'window_days': args.window_days,
                'activity': 'unknown',
                'count_capped': False,
                'error': str(e),
            })

    rows.sort(key=lambda x: (x['activity'], -(x['commits_window'] or -1), x['repo']))

    # JSON
    payload = {
        'generated_at_utc': now.isoformat() + 'Z',
        'window_days': args.window_days,
        'repos_total': len(rows),
        'rows': rows,
    }
    os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
    with open(args.output_json, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # Markdown
    lines = []
    lines.append('# GitHub Activity Report')
    lines.append('')
    lines.append(f'- Generated: `{payload["generated_at_utc"]}`')
    lines.append(f'- Window: `{args.window_days}` days')
    lines.append(f'- Repositories: `{len(rows)}`')
    lines.append('')
    lines.append('## Results')
    lines.append('')
    for r in rows:
        if r['error']:
            lines.append(f"- `{r['repo']}` — status: `unknown`, error: `{r['error']}`")
            continue
        suffix = " (capped at 1000+)" if r.get('count_capped') else ""
        lines.append(
            f"- `{r['repo']}` — activity: `{r['activity']}`, commits/{args.window_days}d: `{r['commits_window']}`{suffix}, "
            f"last: `{r['last_commit_date']}` by `{r['last_commit_author']}` (`{r['last_commit_sha']}`)"
        )

    os.makedirs(os.path.dirname(args.output_md), exist_ok=True)
    with open(args.output_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f"Wrote {args.output_md} and {args.output_json}")


if __name__ == '__main__':
    main()
