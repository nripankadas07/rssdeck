from rssdeck.core import parse_rss, render_dashboard, youtube_channel_feed


def test_rss_dashboard():
    xml = "<rss><channel><item><title>A</title><link>https://a.test</link></item></channel></rss>"
    items = parse_rss(xml, "feed")
    assert items[0].title == "A"
    assert "https://a.test" in render_dashboard(items)
    assert "channel_id=UC123" in youtube_channel_feed("UC123")
