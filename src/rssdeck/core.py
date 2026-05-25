from __future__ import annotations

import html
import xml.etree.ElementTree as ET
from dataclasses import dataclass


@dataclass(frozen=True)
class FeedItem:
    title: str
    link: str
    source: str = ""


def parse_rss(xml_text: str, source: str = "") -> list[FeedItem]:
    root = ET.fromstring(xml_text)
    items: list[FeedItem] = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            items.append(FeedItem(title=title, link=link, source=source))
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = (entry.findtext("{http://www.w3.org/2005/Atom}title") or "").strip()
        link_el = entry.find("{http://www.w3.org/2005/Atom}link")
        link = link_el.attrib.get("href", "") if link_el is not None else ""
        if title and link:
            items.append(FeedItem(title=title, link=link, source=source))
    return items


def youtube_channel_feed(channel_id: str) -> str:
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


def render_dashboard(items: list[FeedItem], title: str = "rssdeck") -> str:
    rows = "\n".join(
        f'<li><a href="{html.escape(item.link)}">{html.escape(item.title)}</a>'
        f'<small>{html.escape(item.source)}</small></li>'
        for item in items
    )
    return f"<!doctype html><title>{html.escape(title)}</title><h1>{html.escape(title)}</h1><ul>{rows}</ul>"
