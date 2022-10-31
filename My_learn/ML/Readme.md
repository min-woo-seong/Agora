# Scikit-lean 라이브러리 소개
```
├─ Estimator(지도학습의 모든 알고리즘)
│  ├─Classifier(분류구현클래스)
│  │  ├─DecisionTreeClassfier
│  │  ├─GaussianNB
│  │  ├─GradientBoostingClassfier
│  │  ├─RandomForestClassfier
│  │  └─SVC
│  └─regressor(회귀구현클래스)
│      ├─GradienBoostingRegressor
│      ├─Lasso
│      ├─LinearRegression
│      ├─RandomForestRegressor
│      └─Ridge
├─fit() [학습]
└─predict() [예측]
```

### -Module

|분류|모듈명|설명|
|------|---|---|
|예제 데이터|**sklearn.datasets** |사이킷런 내장 예제 제공 데이터셋 |
|피처 처리|**sklearn.preprocessing**  |데이터 전처리시 필요한 댜양한 기능 제공(예 : 인코딩, 정규화 스케일링등) |
|  | **sklearn.feature_selection**| 알고리즘 수행시 큰 영향을 미치는 피처를 우선순위대로 선택후 작업을 수행하는 다양한 기능 제공 |
|  | **sklearn.feature_exture_extraction**  |텍스트 데이터나 이미지 데이터의 벡터화된 피처를 추출 |
| 피처 처리& 차원 축소 | **sklearn.decomposition** |차원 축소와 관련한 알고리즘을 지원하는 모듈 (PCA, NMF, Truncate SVD등 |
| 데이터분리, 검증& 파라미터 튜닝 | **sklearn.model_selection** | 교차검증을 위한 학습/테스트용분리, GridSearch로 최적 파라미터 추출등 API제공|
|평가 | **sklearn.metrics** |분류, 회귀, 클러스터링, 페어와이즈에 대한 다양한 성능 측정 방법 제공 (Accuracy, Precision, Recall, ROC-AUC, RMSE) |
|머신러닝 알고리즘  | **sklearn.ensemble**  |앙상블 알고리즘(랜덤포레스트, 에이다 부스트, 그래디언트부스팅 |
|  |**sklearn.linear_model**   |선형 회귀, 릿지, 라쏘및 로지스틱회귀등 회귀 관련 알고리즘을 지원, SGD관련 알고리즘도 제공 |
|  | **sklearn.naive_bayes** |나이브 베이즈 알고리즘 제공, 가우시안, NB, 다항분포NB등 |
|  |**sklearn.neighbors**  |최근접 이웃 알고리즘 제공, K-NN | 
|  | **sklearn.svm** | 서포트 벡터 머신 알고리즘|
|  | **sklearn.tree**  | 의사 결정 트리 알고리즘|
|  |**sklearn.cluste**r  | 비지도 클러스터링 알고리즘 (K-평균, 계층형, DBSCAN등)|
|유틸리티  | **sklearn.pipeline** |피처 처리 등의 변환과 머신러닝 알고리즘학습, 예측 등을 같이 묶어서 실행할 수 있는 유틸리티 |
