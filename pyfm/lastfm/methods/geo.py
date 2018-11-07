from lastfm.methods import apimethod, Limit, Page
from lastfm.models.geo import GeoTopArtists, GeoTopTracks


class Geo:
    """
    Last.fm Geo API interface for easy access/navigation
    """

    def __init__(self, country: str):
        """
        :param str country:  A country name, as defined by the ISO 3166-1 country names standard
        """
        self.country = country

    @apimethod
    def get_top_artists(
        self, limit: Limit = None, page: Page = None
    ) -> GeoTopArtists:
        """
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :returns: GeoTopArtists
        """
        return dict(country=self.country, limit=limit, page=page)

    @apimethod
    def get_top_tracks(
        self, limit: Limit = None, page: Page = None
    ) -> GeoTopTracks:
        """
        :param limit: The number of results to fetch per page. Defaults to 50.
        :param page: The page number to fetch. Defaults to first page.
        :returns: GeoTopArtists
        """
        return dict(country=self.country, limit=limit, page=page)
