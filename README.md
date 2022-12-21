# 서울시 대중교통 유동인구 분석
4학년 2학기 '데이터크롤링' 기말 프로젝트

# <소개>
- OpenAPI를 활용하여 대중교통 교통량을 크롤링하여 서울시 시간별 대중교통 유동인구 분석
- 지오코딩(geoPy)를 활용하여 좌표를 주소화, 주소를 시 군 동으로 분류
- folium 라이브러리 사용하요 유동인구 지도시각화, .geojson 확장자 파일 커스텀 후 시각화에 이용

  ## 데이터 셋
    - <a href = "https://data.seoul.go.kr/dataList/OA-12252/S/1/datasetView.do">서울시 지하철 호선별 역별 시간대별 승하차 인원 정보</a>
    - <a href = "https://data.seoul.go.kr/dataList/OA-12913/S/1/datasetView.do">서울시 버스노선별 정류장별 시간대별 승하차 인원 정보</a>
    - <a href = "https://data.seoul.go.kr/dataList/OA-21232/S/1/datasetView.do">서울시 역사마스터 정보</a>
    - <a href = "https://data.seoul.go.kr/dataList/OA-15067/S/1/datasetView.do">서울시 버스정류소 위치정보</a>
    
  ## 구현
  
    ### 데이터 전처리
    
    - 지하철 역, 정류장 위치별 시간별로 승하차인원 통합
    - 데이터셋 활용하여 지하철 역, 정류장의 x,y 좌표를 역지오코딩하여 상세주소 출력후 지역별로 병합
    
    ### 지도 시각화
    
    - 기존의 .geojson파일을 커스텀 / 세분화된 동 하나의 동으로 병합 (ex > 상계 1동, 상계 2동 ... ->> 상계동)
    - 커스텀된 .geojson을 베이스로 folium 라이브러 활용하여 지도 시각화
    
    ### 결과
    
    - 1시간 단위 서울시의 대중교통으로 인한 유동인구 비율 시각화
    
    - 유동인구가 가장 많은 지역 (2022년 11월 한 달 기준)
      > 강남구 역삼동
      > 강서구 화곡동
      > 양천구 목동
      > 노원구 상계동
      > 서초구 서초동

## <개발환경>
- IDE : Pycharm
- 사용도구 : <a href = "https://qgis.org/ko/site/">QGis(.geojson 커스텀)</a>

    
