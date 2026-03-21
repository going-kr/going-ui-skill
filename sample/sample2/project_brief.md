## 1. 프로젝트 개요

- **프로젝트명**: TemperatureMonitor
- **앱 이름**: TemperatureMonitor
- **목적**: Modbus TCP를 통해 온도 센서 데이터를 실시간 모니터링하고, 트렌드 그래프로 이력을 확인하는 HMI 프로그램
- **해상도**: 800x480
- **테마**: Dark

---

## 2. 화면 구성

### 페이지 목록

#### PageMain
- **역할**: 실시간 온도 모니터링
- **주요 컨트롤**:
  - **GoLabel** x10: 온도 센서 1~10 현재값 표시 (lblTemp0 ~ lblTemp9)
  - **GoLamp** x1: 통신 상태 표시 (lampStatus)
  - **GoProgress** x1: 대표 온도 레벨 바 (progLevel)
  - **GoNavigator**: 페이지 전환 (PageMain / PageHistory)
- **페이지 이동**: GoNavigator로 PageHistory 전환
- **열리는 윈도우**: Settings 버튼 → SettingWindow

#### PageHistory
- **역할**: 온도 트렌드 그래프 표시
- **주요 컨트롤**:
  - **GoTrendGraph** x1: 온도 1~3 트렌드 (trendTemp)
  - **GoNavigator**: 페이지 전환 (PageMain / PageHistory)

### 윈도우(팝업) 목록

#### SettingWindow
- **트리거**: PageMain의 Settings 버튼
- **역할**: Modbus TCP 접속 설정 (IP, Port)
- **주요 컨트롤**:
  - GoInputString: IP 주소 입력
  - GoInputNumber<Int32>: 포트 번호 입력
  - GoButton: 저장(OK), 취소(Cancel)
- **반환값**: 없음 (설정값은 DataManager에 저장)

---

## 3. 통신

### Modbus TCP

- **프로토콜**: MasterTCP
- **IP 주소**: 192.168.0.100
- **포트**: 502
- **타임아웃(ms)**: 1000

**슬레이브 구성**

| 슬레이브 번호 | 역할 |
|-------------|------|
| 1 | 온도 센서 컨트롤러 |

**레지스터 맵 — Data Read (FC3)**

| 주소 | 명칭 | 설명 | 단위 | 데이터형 | R/W | FC |
|------|------|------|------|---------|-----|-----|
| D0 | Temp0 | 온도 센서 1 (-20.0~150.0) | 0.1℃ | Word | R | FC3 |
| D1 | Temp1 | 온도 센서 2 | 0.1℃ | Word | R | FC3 |
| D2 | Temp2 | 온도 센서 3 | 0.1℃ | Word | R | FC3 |
| D3 | Temp3 | 온도 센서 4 | 0.1℃ | Word | R | FC3 |
| D4 | Temp4 | 온도 센서 5 | 0.1℃ | Word | R | FC3 |
| D5 | Temp5 | 온도 센서 6 | 0.1℃ | Word | R | FC3 |
| D6 | Temp6 | 온도 센서 7 | 0.1℃ | Word | R | FC3 |
| D7 | Temp7 | 온도 센서 8 | 0.1℃ | Word | R | FC3 |
| D8 | Temp8 | 온도 센서 9 | 0.1℃ | Word | R | FC3 |
| D9 | Temp9 | 온도 센서 10 | 0.1℃ | Word | R | FC3 |
| D10 | StatusBits | 상태 비트 (bit0=Run, bit1=Alarm, bit2=OverTemp) | - | Bit | R | FC3 |

---

## 4. 설정 파일 (DataManager)

저장/로드할 항목:

| 항목명 | 타입 | 기본값 | 설명 |
|--------|------|--------|------|
| RemoteIP | string | "192.168.0.100" | Modbus TCP 서버 IP |
| RemotePort | int | 502 | Modbus TCP 서버 포트 |
| Timeout | int | 1000 | 통신 타임아웃(ms) |

---

## 5. 배포

- **장치 hostname**: (미정)
- **앱 이름**: TemperatureMonitor
- **자동실행**: Y
- **키오스크 모드**: Y
