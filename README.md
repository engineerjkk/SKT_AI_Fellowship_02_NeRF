# SKT AI Fellowship 5기   
안녕하세요! 저희는 SKT AI Fellowship 5기의 “02. AI 기반 고화질 3D 변환 기술(NeRF:Neural Radiance Fields)” 과제에 참여하게 된 **NeRF Maverick** 팀입니다.    

### 최종 발표 영상 : [클릭](https://youtu.be/oemOx9q-se4?si=15E88MbxjzXxh67b)

저희는 AI를 이용한 3D 변환기술인 NeRF를 Virtual Production에 상용화할 수 있는지 검증하고, 3D 데이터 생성에 대한 메뉴얼과 변환 방법을 정리하였습니다.

저희가 정리한 데이터 생성 메뉴얼과 변환 방법을 이용해 3D 데이터를 생성한 결과, **기존 방법에 비해 제작 시간과 비용을 상당히 절감**할 수 있었습니다.    

![image](https://github.com/user-attachments/assets/2b094891-1068-467f-93d8-ab8ef3314142)    
### Virtual Production이란?  
![image](https://github.com/user-attachments/assets/de5f1d1d-83be-43b1-bfaf-1cc100f31345) 
<center class="half">
    <img src="https://github.com/user-attachments/assets/de5f1d1d-83be-43b1-bfaf-1cc100f31345" title="VP" width="250" height="170"/> 
          <Virtual Production>   

Virtual Production은 가상의 공간을 무대로 만들어, 무대 위에 있는 사람이 마치 그 공간에 있는 것처럼 보이는 영상을 촬영할 수 있는 환경입니다.  
뒤에 있는 LED Wall에 가상 장면을 띄워 놓고, 카메라의 움직임에 따라 자연스럽게 배경이 바뀌게 하여 무대 위의 배우가 더욱 몰입감 있게 연기할 수 있는 장점이 있습니다.  
SKT에서는 TEAM Studio가 이러한 Virtual Production을 구축하여 현재 운영 중에 있습니다.  

---
### Virtual Production에 사용되는 데이터 제작의 문제점
Virtual Studio의 배경은 가상의 3D 모델을 Unity, Unreal Engine과 같은 게임 엔진을 이용해 실시간으로 렌더링됩니다.  
![image](https://github.com/user-attachments/assets/bb1e6d04-41df-4dac-9072-d620d98d4f61)
이 때 사용되는 3D 배경 모델은, 단일 물체 하나하나를 자연스럽게 만들기 위해 전문가가 한 땀, 한 땀 디자인하여 길게는 수 개월 간의 제작 과정을 거치게 됩니다.
이 과정에서 많은 시간과 비용이 소요됩니다.
![image](https://github.com/user-attachments/assets/b5f60e77-f3ad-4be6-bd90-85da59579515)
3D Mesh를 만들어 이를 해결하고자 하는 접근 방법도 있었지만, 보이시는 것과 같이 사진으로부터
3D Mesh를 뽑아내는 방법은 조명 변화에 따라 부자연스럽고, 섬세한 부분에 있어 표현력이 떨어지는 문제가 있었습니다.

---
### NeRF
가상 배경을 만드는 것은 앞의 방법처럼 3D 모델을 만들어 게임 제작 툴에 넣고 가상 카메라를 움직이는 방법으로 만들 수도 있지만, 이러한 딥러닝 모델을 사용할 수도 있습니다.  
![image](https://github.com/user-attachments/assets/8c9f2268-6943-4f9e-b561-28731a5ad5cb)

2020년 ECCV에서 발표된 NeRF는 장면을 다양한 방향에서 촬영한 이미지로 3D 공간의 밝기와 밀도를 표현하는 연속함수를 학습하는 딥러닝 기반의 렌더링 기법입니다.  
이 기법을 사용하면, 카메라로 명소와 같은 곳에 가서 여러 각도로 사진을 찍고, 찍은 사진들을 학습시켜 사용자가 원하는 방향에서 본 장면을 렌더링할 수 있습니다.  
NeRF를 사용하면 하루에서 이틀 정도의 학습을 거쳐, 수 시간의 렌더링을 통해 원하는 카메라 궤적에 따른 동영상을 생성할 수 있습니다.  
그래서 저희는 이 기술을 Virtual Production에 적용해 보고자 하였습니다.
![image](https://github.com/user-attachments/assets/81c6af01-3b42-40af-8c90-93460d227815)
NVIDIA 사의 Instant-NGP 모델은 30분 이내로 학습되고, 한 시간 이내에 고화질 동영상을 생성할 수 있는 개선된 NeRF 모델입니다.
저희는 이 모델을 기본 모델로 하여 연구를 진행했습니다.

--- 
### 연구 목표
SKT TEAM Studio와의 회의와 멘토님들과의 토의를 통해, 다음 네 가지의 목표를 세웠습니다.    

1. NeRF를 위한 촬영 방법에 대한 메뉴얼 제작     
2. NeRF 렌더링의 실시간화    
3. 로봇암을 이용한 Toy Virtual Production 환경 구성    
4. 4K 수준의 고화질 렌더링    
그리고 이러한 목표를 달성하기 위해 다음과 같은 단계로 연구를 진행했습니다.

![image](https://github.com/user-attachments/assets/c424e5cf-a423-4865-8b7d-53f431aa6b44)  

1.효과적인 데이터셋 수집 방법을 탐색하여 메뉴얼 작성    
2.SOTA 모델에 대한 끊임없는 follow-up을 통한 기본 모델의 고도화      
3.추가적인 데이터셋 수집 방법 도입에 따른 최적화된 전처리 기법 모색    
4.3D 게이밍 툴과의 호환을 통한 실시간 고화질 렌더링 실현    
6. 로봇암과 모니터로 구성한 자체 Virtual Production을 구축하여 검증
   
### 연구 과정
**1. 데이터셋 메뉴얼 작성**  
NeRF는 장면을 여러 각도에서 찍은 이미지를 입력으로 하여 3D 공간 정보를 학습합니다. 공간 정보를 학습하는 과정은 공간 기하학적인 계산 과정을 거치는데요,    
데이터를 수집할 때 이미지에 공간의 다양한 정보를 담아야 학습할 때 유리합니다.    
이는 카메라의 궤적과 밀접한 관련이 있기 때문에 저희는 실내와 실외 환경에서 다양한 카메라 궤적으로 데이터를 수집한 뒤 NeRF 모델을 학습시킨 뒤 성능을 비교했습니다.    
![image](https://github.com/user-attachments/assets/3feb6978-8344-46cd-835e-a0deb2842bba)   
여러 가지 궤적과 이들의 조합 중, 위의 그림과 같이 성능이 좋은 궤적과 지양해야 할 궤적을 도출할 수 있었습니다.  
저희는 이를 바탕으로 "NeRF 배경 장면 제작을 위한 최적의 카메라 궤적"이라는 논문을 작성하여, 데이터를 수집할 때의 메뉴얼로 활용할 수 있게 하였습니다.  
실험 페이지 : https://sonbosung.github.io/NeRFMaverick/  

**2. SOTA 모델에 대한 끊임없는 follow-up을 통한 기본 모델의 고도화**  
![image](https://github.com/user-attachments/assets/317ffb08-136c-4e71-b64b-6870a10d55bb)   
저희가 여태까지 사용한 Instant-NGP 모델의 경우, 최신예(state-of-the-art, SOTA) 방법이지만 실시간성과 고화질 결과물이라는 두 마리 토끼를 다 잡을 수는 없었습니다.  
그리하여 새로 나온 방법들을 계속 찾아 적용해보며 개선 가능성을 찾고 있었습니다.  
마침 8월에 Gaussian Splatting이라는 기법이 등장했는데, Gaussian Splatting은 Instant-NGP와 학습 시간은 비슷하지만 10배 가량 빠른 렌더링을 할 수 있어 실시간성이라는 문제를 푸는 열쇠가 되었습니다.  
따라서, 저희는 Gaussian Splatting을 최종 모델로 선택하고 연구를 이어갔습니다.    

**3. 추가적인 데이터셋 수집 방법 도입에 따른 최적화된 전처리 기법 모색**  
Virtual Production에서 역동적인 카메라 움직임이 있는 경우에는, 바닥과 천장 그리고 촬영자의 뒷부분까지도 카메라가 움직일 수 있는데요,  
이러한 상황을 다 대비하여 이미지 데이터셋을 구축할 때 위와 아래, 뒤까지 일일이 촬영하는 것은 비효율적입니다.  
그래서 저희는 360도 전 방향을 한 번에 촬영할 수 있는 360 카메라를 도입했습니다.
![image](https://github.com/user-attachments/assets/b5e56363-2a7b-4327-8760-2465ec711615)  
360 카메라로 촬영을 하면 이와 같은 equirectangular 이미지가 결과물로 나오는데요, 이러한 이미지는 보통 전처리를 거쳐 사용됩니다.    
![image](https://github.com/user-attachments/assets/919b66ca-82fa-4df5-a255-35f2f698d18a)      
위의 사진은 일반적인 전처리 기법을 적용한 Gaussian Splatting 결과물인데요, 성능이 매우 떨어지는 것을 보실 수 있습니다.  
![image](https://github.com/user-attachments/assets/36f9f72d-2266-4a9a-b7a0-9a936cd004cd)  
이후 수많은 실험을 통해 Gaussian Splatting에 가장 적합한 전처리 방법을 찾았고, 이를 토대로 고화질의 결과물을 얻을 수 있었습니다.  
![image](https://github.com/user-attachments/assets/e665461b-4ac1-41b6-9878-720573b9bff6)  

**4. Unity 및 Toy Virtual Production과의 연동**  
![1674ccaa23372e253405ff5fe0637a80d6dcb4710f4a6977f85c90339ec649ed](https://github.com/user-attachments/assets/3dcf26c6-1bf9-4913-bf8f-e5bac34231da)  

Gaussian Splatting은 plugin을 이용하여 3D 게임 엔진인 unity와 연동하여 수정 가능한 3D 배경 모델으로 변환할 수 있습니다.    
이 기술을 이용하면, 학습 과정에서 발생한 노이즈를 제거할 수 있을 뿐만 아니라, 스튜디오의 사용자들 역시 새로운 소프트웨어에 적응할 필요 없이 기존에 사용하던 unity를 그대로 사용할 수 있어 편리합니다.    
![image](https://github.com/user-attachments/assets/7e84f07a-1a29-40f3-be1f-958434fd0446)  
Gaussian Splatting을 unity로 구동하며 실시간 고화질 렌더링을 수행할 수 있다는 것을 보이기 위해 4K 울트라 와이드 모니터와 로봇암으로 Toy Virtual Production을 구성했습니다.    
로봇암과 모니터가 연결된 데스크탑을 소켓 통신으로 연결하여 실시간으로 로봇암의 좌표 정보를 화면에 적용할 수 있게 하였습니다.    
![b9789636858d1e43a442a4b2d2b6ca63dab7dd8cb6de8d790c561f3bca1cd8fc](https://github.com/user-attachments/assets/819349e8-0de1-487e-8923-92e62e8eb5eb)  
손으로 카메라를 직접 움직여 촬영할 수도 있고,    
![9f83a144af688fd178873a743f9ef3844f5428d74ca23dbb209634b494c78e0c](https://github.com/user-attachments/assets/608fafd8-adbf-4723-afb5-b44fb42704b5)  
궤적을 미리 설정해놓고 이에 따라 움직이며 촬영할 수도 있습니다.    
이렇게 하여 Virtual Production에서의 활용 가능성 역시 검증할 수 있었습니다.    
### 연구 결과
![image](https://github.com/user-attachments/assets/3437a205-83bf-422d-bf95-13aa502e0929)  

이렇게 계획한 내용에 대한 연구를 모두 훌륭히 마쳤습니다.    
1. 기존의 3D Asset을 이용하여 NeRF를 적용했을 때에 성능 차이가 거의 없음을 확인하였으며,    
2. 시간대에 따른 조명 및 계절 변화와 같은 수정 가능성도 확인하였습니다.
3. NeRF를 위한 촬영 방법에 대한 메뉴얼을 제작하고,  
4. NeRF의 실시간 렌더링 가능성 및    
5. 4K 수준의 고화질 렌더링 가능성을  
7. 로봇암을 이용한 Toy Virtual Production을 구성하여 확인했습니다.
  
마지막으로 실제 SKT TEAM Studio에서 시연한 영상입니다.     
![753f92a3d736fd6fadaa1799ffd75f5af143dde96a34af04d44e96ed94d36fbe](https://github.com/user-attachments/assets/43a3df55-ee8d-4519-93a0-65e69d5bd364)     

(이번 게시물의 모든 시연 영상은 용량 제한으로 많이 압축된 점 양해 부탁드립니다.)  
---
  
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
  
 </div>
 노션 팀 페이지 : [Notion](https://www.notion.so/df7bab012c9d41aabead43d3adc8aeb5?v=3efdecb091204417b03e56297ff8c612)  

IQA_PyTorch 원본 링크 : [IQA_PyTorch ](https://github.com/chaofengc/IQA-PyTorch#zap-quick-start)  

LPIPS, BRISQUE 계산 코드 : IQA_PyTorch/IQA.ipynb  
- 세번째 셀부터 실행시키시면 되고, **자동화** 아래의 셀이 LPIPS와 BRISQUE를 계산하여 저장하는 셀입니다.
- 원본이미지와 렌더링 이미지 그리고 PSNR, SSIM이 저장된 result.csv 파일이 있는 폴더의 경로를 설정해주시면 됩니다. 
-->

