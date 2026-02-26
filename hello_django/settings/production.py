from .base import *
import os

# EB내부에서 ALB가 EC2에 대한 헬스체크 요청대비
# - EC2 사설ip로 요청하는 경우 Disallowed Host 오류발생
# - ebhealthcheck앱이 현재 EC2의 사설ip를 자동으로 ALLOWED_HOSTS에 등록
INSTALLED_APPS.extend([
    'ebhealthcheck.apps.EBHealthCheckConfig',
])

DEBUG = False

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '.amazonaws.com'
]

# 추가 ALLOWED_HOSTS 설정
additional_allowed_hosts = os.getenv('ALLOWED_HOSTS')
if additional_allowed_hosts:
    ALLOWED_HOSTS.extend([host.strip() for host in additional_allowed_hosts.split(',')])

print(f'[production] {ALLOWED_HOSTS = }')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}