from attr import dataclass

from pydrag.core import ApiMixin, BaseModel


@dataclass
class AuthSession(BaseModel, ApiMixin):
    key: str
    name: str

    @classmethod
    def get(cls) -> "AuthSession":
        """
        Create a web service session for a user.

        :rtype: :class:`~pydrag.lastfm.models.auth.AuthSession`
        """
        return cls.submit(
            bind=AuthSession,
            authenticate=True,
            params=dict(method="auth.getMobileSession"),
        )
