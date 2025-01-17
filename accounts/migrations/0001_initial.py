# Generated by Django 3.2 on 2021-05-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.CharField(max_length=12, unique=True, verbose_name='User ID')),
                ('major', models.CharField(choices=[('인문과학대학', (('국어국문학과', '국어국문학과'), ('영어영문학과', '영어영문학과'), ('독일어문ㆍ문화학과', '독일어문ㆍ문화학과'), ('프랑스어문 ㆍ 문화학과', '프랑스어문 ㆍ 문화학과'), ('일본어문ㆍ문화학과', '일본어문ㆍ문화학과'), ('중국어문ㆍ문화학과', '중국어문ㆍ문화학과'), ('사학과', '사학과'))), ('사회과학대학', (('정치외교학과', '정치외교학과'), ('심리학과', '심리학과'), ('지리학과', '지리학과'), ('경제학과', '경제학과'), ('경영학과', '경영학과'), ('경영학부', '경영학부'), ('미디어커뮤니케이션학과', '미디어커뮤니케이션학과'), ('사회복지학과', '사회복지학과'))), ('법과대학', (('법학과', '법학과'), ('지식산업법학과', '지식산업법학과'), ('법학부', '법학부'))), ('자연과학대학', (('수학과', ' 수학과'), ('통계학과', '통계학과'), ('화학과', '화학과'), ('생명과학ㆍ화학부', '생명과학ㆍ화학부'), ('수리통계데이터사이언스학부', '수리통계데이터사이언스학부'), ('화학ㆍ에너지융합학부', '화학ㆍ에너지융합학부'))), ('지식서비스공과대학', (('청정융합에너지공학과', '청정융합에너지공학과'), ('바이오생명공학과', '바이오생명공학과'), ('바이오식품공학과', '바이오식품공학과'), ('융합보안공학과', '융합보안공학과'), ('컴퓨터공학과', '컴퓨터공학과'), ('정보시스템공학과', '정보시스템공학과'), ('서비스ㆍ디자인공학과', '서비스ㆍ디자인공학과'), ('AI융합학부', 'AI융합학부'))), ('간호대학', (('간호학과', '간호학과'),)), ('HEALTH & WELLNESS COLLEGE', (('스포츠레저학과', '스포츠레저학과'), ('운동재활복지학과', '운동재활복지학과'), ('글로벌의과학과', '글로벌의과학과'), ('식품영양학과', '식품영양학과'), ('스포츠과학부', '스포츠과학부'))), ('뷰티생활산업국제대학', (('글로벌비즈니스학과', '글로벌비즈니스학과'), ('의류산업학과', '의류산업학과'), ('뷰티산업학과', '뷰티산업학과'), ('소비자생활문화산업학과', '소비자생활문화산업학과'))), ('사범대학', (('교육학과', '교육학과'), ('사회교육과', '사회교육과'), ('윤리교육과', '윤리교육과'), ('한문교육과', '한문교육과'), ('유아교육과', '유아교육과'))), ('미술대학', (('동양화과', '동양화과'), ('서양화과', '서양화과'), ('조소과', '조소과'), ('공예과', '공예과'), ('산업디자인과', '산업디자인과'))), ('음악대학', (('성악과', '성악과'), ('기악과', '기악과'), ('작곡과', '작곡과'))), ('융합문화예술대학', (('문화예술경영학과', '문화예술경영학과'), ('미디어영상연기학과', '미디어영상연기학과'), ('현대실용음악학과', '현대실용음악학과'), ('무용예술학과', '무용예술학과')))], default='국어국문학과', max_length=15)),
                ('studentId', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
