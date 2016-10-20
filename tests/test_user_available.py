def test_user_available(User):
        username = User('foo')
        assert username.exists


def test_user2_available(User):
        username = User('bar')
        assert username.exists
