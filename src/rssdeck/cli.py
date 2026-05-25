from __future__ import annotations

import argparse
import sys
from .core import parse_rss, render_dashboard, youtube_channel_feed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render RSS into a private dashboard.")
    parser.add_argument("--youtube-channel")
    parser.add_argument("--title", default="rssdeck")
    args = parser.parse_args(argv)
    if args.youtube_channel:
        print(youtube_channel_feed(args.youtube_channel))
        return 0
    items = parse_rss(sys.stdin.read(), source="stdin")
    print(render_dashboard(items, args.title))
    return 0
