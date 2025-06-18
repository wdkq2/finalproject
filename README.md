# roboadivser

간단한 로보 어드바이저 예제입니다. 시나리오 기반 투자와 특징 검색 기능을 간단하게 체험할 수 있는 웹 인터페이스를 제공합니다.

## 실행 방법 (Colab)
1. 새로운 Colab 노트를 열고 아래 명령을 실행해 저장소를 클론합니다. `clone_repo.py`
   스크립트는 `work` 브랜치가 존재하면 해당 브랜치를, 그렇지 않으면 기본 브랜치를
   자동으로 선택해 클론합니다.
```python
!python clone_repo.py <저장소 URL>
%cd roboadivser
```
다음 명령으로 파일 목록을 확인했을 때 `requirements.txt` 가 보이지 않는다면
올바른 브랜치가 선택되지 않은 것이므로 저장소 URL을 확인해 주세요.
```python
!ls
```
2. 필요한 패키지를 설치합니다. 위에서 `requirements.txt` 가 보이는 위치에서 실행하세요.
```python
!pip install -r requirements.txt
```
3. 앱을 실행합니다. `share=True` 옵션이 적용되어 실행 후 공개 링크가 표시됩니다.
```python
!python app.py
```
   셀이 실행된 상태를 유지한 채로 "Running on public URL" 다음에 나타나는 링크를 
   클릭하면 웹 인터페이스를 확인할 수 있습니다.

## 주요 기능
- **시나리오 투자 탭**: 시나리오 내용과 주문 수량, 뉴스 검색 키워드를 입력하면 시나리오가 기록됩니다. "최신 뉴스 확인" 버튼을 누르면 해당 키워드로 구글 뉴스를 검색해 상위 기사 제목과 링크를 보여줍니다.
- **시나리오 저장소 탭**: 매매가 완료된 시나리오와 거래 정보를 표 형식으로 확인할 수 있습니다.
- **특징 검색 탭**: 자연어로 작성된 프롬프트를 해석해 샘플 데이터에서 종목을 추천하고, 필요하다면 매매 API로 거래를 실행합니다.

실제 API를 사용하려면 실행 전에 다음 환경 변수를 설정해야 합니다. 기본값은 예제 키이며, 계좌번호는 코드에 기본값(12345678)이 있으므로 필요하면 `TRADE_ACCOUNT` 환경 변수로 변경할 수 있습니다. 또한 필요하다면 매매 API URL도 지정합니다.
```python
import os
os.environ["NEWS_API_KEY"] = "<뉴스 API 키>"  # 선택 사항
os.environ["DART_API_KEY"] = "4bada9597f370d2896444b492c3a92ff9c2d8f96"  # DART 키
os.environ["TRADE_API_KEY"] = "PShKdxdOkJXLjBKTVLAbh2c2V5RrX3klIRXv"  # 앱 키
os.environ["TRADE_API_SECRET"] = "Vt/gy4uGEAhWT2Tn0DE6IK2u+CBt752yHht/VXcjJUk7NzgZkx3lVoSDHvj/G2+RZNxBBjxEn2ReYQKquoh5BJi9f4KKomsYxJ3cyQ6noTyb0ep1OHD/xIe3w2Y9h+eb0PG7hxwhZBmWwPO6VQq9KRXZockUH5qNTbDosA6mfbKssmxWL2o="  # 앱 시크릿
os.environ["TRADE_PRODUCT_CODE"] = "01"  # 계좌상품코드
os.environ["TRADE_API_URL"] = "https://openapivts.koreainvestment.com:29443"  # 모의투자 URL
```

매매 버튼을 누르면 모의투자 API로 주문이 전송됩니다. 앱 키는 환경 변수로 지정하고 계좌번호는 코드 기본값을 사용하되 `TRADE_ACCOUNT` 환경 변수로 변경할 수 있습니다. 웹 인터페이스에서는 종목 코드와 수량만 입력하면 됩니다. 주문이 완료되면 "시나리오 저장소" 탭에서 모든 거래 내역을 확인할 수 있습니다.
