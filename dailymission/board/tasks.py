import logging
from celery import shared_task
from board.models import UserProfile  # UserProfile 모델이 있는 위치에 따라 경로 조정

# 로깅 설정
logger = logging.getLogger(__name__)


@shared_task
def reset_has_posted_status():
    # 미션 성공 게시판의 게시글 작성 상태 초기화 작업 시작 로그
    logger.info("미션 성공 게시판에서 사용자의 게시글 작성 상태를 초기화합니다.")

    # 게시글 작성 상태가 True인 사용자 프로필을 모두 가져와 초기화
    profiles = UserProfile.objects.filter(has_posted_in_mission_success=True)
    profiles.update(has_posted_in_mission_success=False)

    # 초기화 완료 로그
    logger.info("사용자의 게시글 작성 상태 초기화가 완료되었습니다.")
