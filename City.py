import streamlit as st

from PIL import Image

st.divider()
st.write('# E-WAVE CITY')
st.write('##### LIGHTNING WORLD')
st.write('')
st.divider()

st.write('# 1. VISION')

image2 = Image.open('CitySkyView.jpg')
st.image(image2)
st.write('## "우리의 뜻으로 세상을 공명하자"')
st.write('#### "Resonate the World"')
st.divider()

st.write('')
st.write('###### 공명의 ‘명’은 明으로 도시의 밝은 미래를 뜻하기도 하고, 물리학에서 "공명진동수"의 의미에서 작은 힘의 작용에도 큰 에너지를 전달할 수 있음을 뜻합니다. 우리의 목표는 세상과 잘 맞는, 세상에게 큰 에너지를 주는 것입니다.')
st.divider()

st.write('# 2. DESIGN')

image3 = Image.open('City설계도.jpg')
st.image(image3)

st.divider()

st.write('### 1. 에너지 발전')
st.write('###### 도로에 압전소자를 내장해 압력이 가해질 때마다 전기 에너지를 생성하는 도로, 태양광을 전기 에너지로 전환하는 태양광 패널, 바람을 전기 에너지로 전환하는 풍력 발전소, 수소와 같은 원자들을 고온&고압의 환경에 두어 핵융합을 시켰을 때 발생하는 손실 에너지를 이용하는 핵융합 발전 설비를 설치하여 친환경적인 에너지를 생산합니다.')
st.divider()

st.write('### 2. 삶의 질 개선')
st.write('###### 수도 시설을 곳곳에 설치하여 기업 및 연구소, 시민들에게 깨끗한 물을 제공합니다. 건물 옥상이나 정밀 농업지에 좋은 수질의 물을 제공하여 농작물을 기르고 소비합니다. 직업 훈련 단지를 건설하여 시민들로 하여금 일자리를 얻기 위한 능력을 길러줍니다.')
st.divider()

st.write('### 3. 미래를 위한 연구')
st.write('###### 핵융합 연구소, 의료기기 연구소, 바이오 연구소, 탄소 포집 활용소 등을 건설하여 도시가 점점 발전할 수 있는 토대를 마련하고, 자원 순환 재배기술 연구 및 지자체 확산을 위한 교육을 운영합니다.')
