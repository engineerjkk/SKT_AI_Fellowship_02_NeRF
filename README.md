# SKT_AI_Fellowship_02_NeRF
(업데이트 예정. 2024.07.11)   
안녕하세요! 저희는 SKT AI Fellowship 5기의 “02. AI 기반 고화질 3D 변환 기술(NeRF:Neural Radiance Fields)” 과제에 참여하게 된 NeRF Maverick 팀입니다.   
   
노션 팀 페이지 : [Notion](https://www.notion.so/df7bab012c9d41aabead43d3adc8aeb5?v=3efdecb091204417b03e56297ff8c612)

IQA_PyTorch 원본 링크 : [IQA_PyTorch ](https://github.com/chaofengc/IQA-PyTorch#zap-quick-start)

LPIPS, BRISQUE 계산 코드 : IQA_PyTorch/IQA.ipynb  
- 세번째 셀부터 실행시키시면 되고, **자동화** 아래의 셀이 LPIPS와 BRISQUE를 계산하여 저장하는 셀입니다.
- 원본이미지와 렌더링 이미지 그리고 PSNR, SSIM이 저장된 result.csv 파일이 있는 폴더의 경로를 설정해주시면 됩니다. 

# 로봇암
- 메인 코드만 업로드하였습니다. 함수로 되어 더 필요한 파일이 있지만 양이 많아 우선 이정도만 업데이트 합니다.
- 비록 Server 로봇암이 저희가 가지고 있는 로봇암에서만 동작하지만, 어느정도 큰 틀은 다른 로봇암과 유사할 거라고 생각합니다.  
### Client(윈도우 유니티)
- UnityClient6DoF.cs
  - 로봇암 서버로부터 6DoF 데이터를 받아 스케일 조정을 한 뒤, 유니티 가상 카메라 좌표에 입력합니다.
### Server (로봇암)
- SetCameraTrajectories.py
  - 카메라 궤적을 손으로 세팅하면, 해당하는 궤적을 pickle 파일로 저장합니다.
- TestCameraTrajectories.py
  - 저장한 pickle 파일을 불러와 로봇암을 동작시키며, 동시에 Client인 유니티에 전송합니다.
- socket_realTime.py
  - 실시간으로 움직이는 카메라 궤적을 Client인 유니티에 전송합니다.

# 최종 발표 영상
[클릭](https://youtu.be/oemOx9q-se4?si=15E88MbxjzXxh67b)
