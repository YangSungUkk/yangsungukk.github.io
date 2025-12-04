import shutil
import os

# 1. Move Image
src = r"C:\Users\didtj\.gemini\antigravity\brain\3136dc07-5961-4b99-b489-42c09dabc11e\intro_bg_1764853439787.png"
dst = r"c:\git\my_portfolio\img\intro-bg.jpg"
try:
    shutil.copy2(src, dst)
    print("Image moved successfully.")
except Exception as e:
    print(f"Error moving image: {e}")

# 2. Update index.html
file_path = r"c:\git\my_portfolio\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Intro Headline
    if 'class="intro-title mb-4"' in line and '양성욱' in line:
        new_lines.append(line.replace('저는 **AI와 데이터를 통해 안전을 혁신하는 양성욱**입니다.', 'AI 기반 안전 예방 시스템을 설계하는 융합 인재, 양성욱입니다'))
    
    # Intro Slogan
    elif '<span class="text-slider-items">' in line:
        new_lines.append(line.replace('안전 시스템 구축, 위험성 평가 전문가,AI 기반 업무 자동화,법규 준수 자동화 시스템,산업안전보건', '산업안전보건 전문가,생성형 AI 기반 업무 자동화,데이터 기반 위험 예측,안전 시스템 디지털 전환'))
    
    # About Me - Job
    elif '<span class="title-s">직무/관심 분야: </span>' in line:
        new_lines.append(line.replace('직무/관심 분야: </span> <span>안전관리 및 AI/데이터 분석</span>', '직무: </span> <span>안전관리자 / AI & 데이터 분석가</span>'))
    
    # About Me - Certifications
    elif '<span class="title-s">GitHub: </span>' in line:
        new_lines.append(line)
        # Add Certifications after GitHub
        indent = line[:line.find('<')]
        new_lines.append(f'{indent}<p><span class="title-s">자격증: </span> <span>산업안전기사, 빅데이터 분석기사 (필기), ISO 45001 심사원 보</span></p>\n')
    
    # Skills
    elif '**산업안전보건법 이해**' in line:
        new_lines.append(line.replace('**산업안전보건법 이해**', '**산업안전보건법 및 ISO 45001** (HSE 매뉴얼 디지털화)'))
    elif '**ISO 45001/PSM 운영**' in line:
        new_lines.append(line.replace('**ISO 45001/PSM 운영**', '**안전보건경영시스템 운영** (법규 매핑 자동화)'))
    elif '**데이터 분석 (Python/R)**' in line:
        new_lines.append(line.replace('**데이터 분석 (Python/R)**', '**데이터 분석 (Python/R)** (사고 기록 데이터 시각화)'))
    elif '**AI/웹 크롤링 자동화**' in line:
        new_lines.append(line.replace('**AI/웹 크롤링 자동화**', '**AI/웹 크롤링 자동화** (위험성 평가 추천 기능)'))
    
    # About Me - Description
    elif '저는 **안전 관리 전문 지식**과' in line:
        new_lines.append(line.replace('저는 **안전 관리 전문 지식**과 **데이터/AI 자동화 역량**을 결합하여, 사업장의 위험을 사전에 예측하고 선제적으로 대응하는 **차세대', '저는 **산업안전공학**을 전공하고 **데이터 분석 및 AI**를 부전공하며, **안전 데이터 기반의 위험 예측 모델 개발**에 주력해 온 융합 인재입니다.'))
    elif '안전 전문가** 양성욱입니다.' in line:
        # This line might be part of the previous paragraph or separate.
        # Based on view_file, it was:
        # 140: ... **차세대
        # 141: 안전 전문가** 양성욱입니다.
        # So I need to handle the second line if I replaced the first one.
        # Actually, I'll just skip this line if I replaced the previous one? No.
        # The replacement above was for line 140.
        # Line 141 is "안전 전문가** 양성욱입니다."
        # I should probably just replace the whole paragraph if I can.
        # But let's just replace the content.
        new_lines.append(line.replace('안전 전문가** 양성욱입니다.', '')) # Remove this part as it's covered in the new text?
        # Wait, the new text "저는 ... 융합 인재입니다." is one sentence.
        # The original was split across lines.
        # If I replace line 140 with the full sentence, line 141 becomes redundant or needs to be removed.
        pass # I will handle this by checking if the previous line was the one I replaced.
    
    # Services
    elif 'ISO 45001 (안전보건경영시스템) 심사원 경험 기반의 시스템 구축 및 개선' in line:
        new_lines.append(line.replace('ISO 45001 (안전보건경영시스템) 심사원 경험 기반의 시스템 구축 및 개선, 안전보건위원회 간사 역할 수행.', 'ISO 45001 심사원 보 자격을 보유하고 있으며, 학교 프로젝트에서 HSE 매뉴얼 디지털화 및 법규 매핑(Mapping) 자동화를 시도했습니다.'))
    elif '**웹 크롤링 및 LLM**을 활용한 **입법 예고 자동 모니터링**' in line:
        new_lines.append(line.replace('**웹 크롤링 및 LLM**을 활용한 **입법 예고 자동 모니터링**, 보고서 생성 자동화 등 행정 업무 효율화 구현.', '**산업안전보건기준에 관한 규칙(KOSHA Rule) 기반의 위험성 평가 항목 추천 기능**을 구현하고, 입법 예고 모니터링 자동화를 수행했습니다.'))
    elif 'Python, SQL 등을 활용한 사고 및 위험성 평가 데이터를 수집' in line:
        new_lines.append(line.replace('Python, SQL 등을 활용한 사고 및 위험성 평가 데이터를 수집, 분석, 시각화하여 선제적인 안전 대책 제시.', 'Python의 Scikit-learn 라이브러리를 사용하여 재해 발생 요인에 대한 분류/회귀 분석을 시도하고, 데이터 기반의 안전 대책을 제시합니다.'))
    
    # Project Links
    elif 'href="img/project-1-detail.jpg"' in line:
        new_lines.append(line.replace('img/project-1-detail.jpg', 'project-1.html'))
    elif 'href="img/project-2-detail.jpg"' in line:
        new_lines.append(line.replace('img/project-2-detail.jpg', 'project-2.html'))
    elif 'href="img/project-3-detail.jpg"' in line:
        new_lines.append(line.replace('img/project-3-detail.jpg', 'project-3.html'))
        
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("index.html updated successfully.")
