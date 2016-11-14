from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_user_available(User):
        username = User('foo')
        assert username.exists


def test_user2_available(User):
        username = User('bar')
        assert username.exists
