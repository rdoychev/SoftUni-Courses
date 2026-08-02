from tarfile import TarError


def check_record(s: str) -> bool:
    a_count = s.count('A')
    l_count = s.count('LLL')

    if a_count > 1 or l_count > 0:
        return False
    return True


s1 = "PPLL"
print(check_record(s1))