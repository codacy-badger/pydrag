from typing import List, Optional

from attr import dataclass

from pydrag.core import BaseModel
from pydrag.lastfm.models.common import Chart, Wiki


@dataclass
class Tag(BaseModel):
    """
    Last.FM tag, chart and geo api client.

    :param name: Tag name
    :param reach: NOIDEA
    :param url: Last.fm tag url
    :param taggings: Number of tagged objects
    :param count: NOIDEA
    :param total: NOIDEA
    :param wiki: Track wiki information
    """

    name: str
    reach: Optional[int] = None
    url: Optional[str] = None
    taggings: Optional[int] = None
    count: Optional[int] = None
    total: Optional[int] = None
    wiki: Optional[Wiki] = None

    @classmethod
    def from_dict(cls, data: dict):
        if "wiki" in data:
            data["wiki"] = Wiki.from_dict(data["wiki"])
        return super(Tag, cls).from_dict(data)

    @classmethod
    def find(cls, name: str, lang: str = None) -> "Tag":
        """
        Get the metadata for a tag.

        :param name: The tag name
        :param lang: The language to return the wiki in, ISO-639
        :rtype: :class:`~pydrag.lastfm.models.tag.Tag`
        """
        return cls.retrieve(
            params=dict(method="tag.getInfo", tag=name, lang=lang)
        )

    @classmethod
    def get_top_tags(cls, limit: int = 50, page: int = 1) -> List["Tag"]:
        """
        Fetches the top global tags on Last.fm, sorted by popularity Old school
        pagination on this endpoint, keep uniformity.

        :param limit: The number of results to fetch per page.
        :param page: The page number to fetch.
        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.tag.Tag`
        """
        return cls.retrieve(
            bind=Tag,
            many="tag",
            params=dict(
                method="tag.getTopTags",
                num_res=limit,
                offset=((page - 1) * limit),
            ),
        )

    @classmethod
    def get_top_tags_chart(cls, limit: int = 50, page: int = 1) -> List["Tag"]:
        """
        Get the top tags chart.

        :param limit: The number of results to fetch per page.
        :param page: The page number to fetch.
        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.tag.Tag`
        """
        return cls.retrieve(
            bind=Tag,
            many="tag",
            params=dict(method="chart.getTopTags", limit=limit, page=page),
        )

    def get_similar(self) -> List["Tag"]:
        """
        Search for tags similar to this one. Returns tags ranked by similarity,
        based on listening data.

        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.tag.Tag`
        """
        return self.retrieve(
            bind=Tag,
            many="tag",
            params=dict(method="tag.getSimilar", tag=self.name),
        )

    def get_top_albums(self, limit: int = 50, page: int = 1) -> List:
        """
        Get the top albums tagged by this tag, ordered by tag count.

        :param limit: The number of results to fetch per page.
        :param page: The page number to fetch.
        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.album.Album`
        """
        from pydrag.lastfm.models.album import Album

        return self.retrieve(
            bind=Album,
            many="album",
            params=dict(
                method="tag.getTopAlbums",
                tag=self.name,
                limit=limit,
                page=page,
            ),
        )

    def get_top_artists(self, limit: int = 50, page: int = 1) -> List:
        """
        Get the top artists tagged by this tag, ordered by tag count.

        :param limit: The number of results to fetch per page.
        :param page: The page number to fetch.
        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.artist.Artist`
        """
        from pydrag.lastfm.models.artist import Artist

        return self.retrieve(
            bind=Artist,
            many="artist",
            params=dict(
                method="tag.getTopArtists",
                tag=self.name,
                limit=limit,
                page=page,
            ),
        )

    def get_top_tracks(self, limit: int = 50, page: int = 1) -> List:
        """
        Get the top tracks tagged by this tag, ordered by tag count.

        :param limit: The number of results to fetch per page.
        :param page: The page number to fetch.
        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.track.Track`
        """
        from pydrag.lastfm.models.track import Track

        return self.retrieve(
            bind=Track,
            many="track",
            params=dict(
                method="tag.getTopTracks",
                tag=self.name,
                limit=limit,
                page=page,
            ),
        )

    def get_weekly_chart_list(self) -> List[Chart]:
        """
        Get a list of available charts for this tag, expressed as date ranges
        which can be sent to the chart services.

        :rtype: :class:`list` of :class:`~pydrag.lastfm.models.common.Chart`
        """
        return self.retrieve(
            bind=Chart,
            many="chart",
            params=dict(method="tag.getWeeklyChartList", tag=self.name),
        )
