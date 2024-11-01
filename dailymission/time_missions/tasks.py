import os
import django
import random
from celery import Celery
from .models import DailyMission
import logging

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailymission.settings')
django.setup()

# Celery 애플리케이션 초기화
app = Celery('dailymission',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# 로깅 설정
logger = logging.getLogger(__name__)


@app.task
def change_mission():
    logger.info("Updating mission...")
    try:
        mission_count = DailyMission.objects.count()
        if mission_count > 0:
            # 현재 활성화된 미션 찾기
            current_active_mission = DailyMission.objects.filter(is_active=True).first()
            current_mission_id = current_active_mission.id if current_active_mission else None

            logger.info(f"Current active mission ID: {current_mission_id}")  # 현재 활성화된 미션 ID 로그

            # 랜덤으로 하나의 미션 선택
            new_mission = None

            while new_mission is None or (current_mission_id is not None and new_mission.id == current_mission_id):
                random_index = random.randint(0, mission_count - 1)
                new_mission = DailyMission.objects.all()[random_index]
                logger.info(f"Selected mission ID: {new_mission.id}")  # 선택된 미션 ID 로그

            # 선택된 미션의 is_active를 True로 설정
            new_mission.is_active = True
            new_mission.save()

            # 나머지 미션의 is_active를 False로 설정
            DailyMission.objects.exclude(id=new_mission.id).update(is_active=False)

            logger.info("Mission updated successfully.")
        else:
            logger.info("No mission found to update.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


