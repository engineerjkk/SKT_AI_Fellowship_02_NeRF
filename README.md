# SKT AI Fellowship 5기 - NeRF Maverick 팀 🎯
> AI 기반 고화질 3D 변환 기술(NeRF: Neural Radiance Fields) 연구

## 🔍 주요 링크
- [📺 최종 발표 영상](https://youtu.be/oemOx9q-se4?si=15E88MbxjzXxh67b)
- [📝 연구계획](https://devocean.sk.com/blog/techBoardDetail.do?ID=165048&boardType=techBlog&searchData=&id=&vcode=&vcodeList=)
- [📊 연구과정](https://devocean.sk.com/community/detail.do?ID=165263&boardType=AI_FELLOWSHIP&page=1)
- [📈 연구결과](https://devocean.sk.com/blog/techBoardDetail.do?page=&query=&ID=165437&boardType=writer&searchData=sonbosung&subIndex=&idList=&pnwriterID=sonbosung)

## 💡 프로젝트 개요
NeRF 기술을 Virtual Production에 상용화하기 위한 검증 및 데이터 생성 메뉴얼 개발 프로젝트

### Virtual Production 소개
<p align="center">
  <img src="https://github.com/user-attachments/assets/de5f1d1d-83be-43b1-bfaf-1cc100f31345" alt="Virtual Production 개념">
</p>

- LED Wall을 활용한 실시간 가상 배경 구현
- 카메라 움직임에 따른 자연스러운 배경 전환
- SKT TEAM Studio 운영 중

### 기존 문제점
<p align="center">
  <img src="https://github.com/user-attachments/assets/bb1e6d04-41df-4dac-9072-d620d98d4f61" alt="문제점">
</p>

1. 3D 모델 제작의 긴 소요 시간 (수개월)
2. 높은 제작 비용
3. 기존 3D Mesh 방식의 한계
   - 조명 변화에 따른 부자연스러움
   - 섬세한 표현의 한계

## 🎯 연구 목표
1. NeRF 촬영 메뉴얼 제작
2. 실시간 렌더링 구현
3. 로봇암 기반 Toy Virtual Production 환경 구축
4. 4K 고화질 렌더링 실현

## 📚 연구 과정

### 1. 데이터셋 메뉴얼 작성
<p align="center">
  <img src="https://github.com/user-attachments/assets/3feb6978-8344-46cd-835e-a0deb2842bba" alt="카메라 궤적">
</p>

- 실내/외 환경별 최적 카메라 궤적 도출
- "NeRF 배경 장면 제작을 위한 최적의 카메라 궤적" 논문 작성
- [🔗 실험 페이지](https://sonbosung.github.io/NeRFMaverick/)

### 2. SOTA 모델 분석 및 개선
<p align="center">
  <img src="https://github.com/user-attachments/assets/317ffb08-136c-4e71-b64b-6870a10d55bb" alt="모델 비교">
</p>

- Instant-NGP에서 Gaussian Splatting으로 전환
- 렌더링 속도 10배 향상
- 실시간성과 고화질 동시 구현

### 3. 360도 카메라 도입 및 최적화
<p align="center">
  <img src="https://github.com/user-attachments/assets/e665461b-4ac1-41b6-9878-720573b9bff6" alt="360도 카메라 결과">
</p>

- 360도 전방향 촬영으로 효율성 향상
- Gaussian Splatting 맞춤형 전처리 기법 개발
- 고화질 결과물 도출

### 4. Unity 연동 및 실시간 렌더링
<p align="center">
  <img src="https://github.com/user-attachments/assets/3dcf26c6-1bf9-4913-bf8f-e5bac34231da" alt="Unity 연동">
</p>

- Unity Plugin 개발
- 로봇암 기반 Toy Virtual Production 구현
- 실시간 4K 렌더링 구현

## 🔧 로봇암 구현 상세
### Client (Unity)
- `UnityClient6DoF.cs`: 6DoF 데이터 처리 및 가상 카메라 제어

### Server (로봇암)
1. `SetCameraTrajectories.py`
   - 카메라 궤적 설정 및 저장
2. `TestCameraTrajectories.py`
   - 저장된 궤적 실행 및 Unity 연동
3. `socket_realTime.py`
   - 실시간 카메라 궤적 전송

## 📊 연구 결과
<p align="center">
  <img src="https://github.com/user-attachments/assets/3437a205-83bf-422d-bf95-13aa502e0929" alt="연구 결과">
</p>

1. 기존 3D Asset 대비 동등 이상의 성능 확인
2. 조명 및 계절 변화 수정 가능성 검증
3. 촬영 메뉴얼 완성
4. 실시간 4K 렌더링 구현
5. SKT TEAM Studio 실제 환경 검증

## 🔗 추가 자료
- [📘 노션 팀 페이지](https://www.notion.so/df7bab012c9d41aabead43d3adc8aeb5?v=3efdecb091204417b03e56297ff8c612)
- [⚡ IQA_PyTorch 원본](https://github.com/chaofengc/IQA-PyTorch#zap-quick-start)
- LPIPS, BRISQUE 계산 코드: `IQA_PyTorch/IQA.ipynb`
