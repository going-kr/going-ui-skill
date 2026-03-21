# LS Electric CNet API Reference

네임스페이스 `Going.Basis.Communications.LS` — LS Electric PLC CNet 프로토콜 시리얼 통신.

---

## CNetFunc (enum)

CNet 통신 함수 코드.

| Name | Description |
|------|-------------|
| NONE | 없음 |
| READ_SINGLE | 단일 읽기 |
| READ_BLOCK | 블록 읽기 |
| WRITE_SINGLE | 단일 쓰기 |
| WRITE_BLOCK | 블록 쓰기 |

---

## CNetValue

`public class CNetValue`

쓰기 요청 시 디바이스 주소와 값을 묶는 데이터 클래스.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| CNetValue | (string dev, int value) | 디바이스 주소와 값으로 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Device | 디바이스 주소 문자열 (예: "D0100") (get) | — |
| int | Value | 쓸 정수 값 (get) | — |

---

## SchedulerStopException

`public class SchedulerStopException : Exception`

시리얼 포트 오류 시 스케줄러 루프를 중단하기 위한 내부 예외.
IOException, UnauthorizedAccessException 등 시리얼 통신 오류 발생 시 throw 되어 Process 루프를 종료한다.

---

## CNet

`public class CNet : IDisposable`

LS Electric PLC CNet 프로토콜 시리얼 통신 클라이언트. 자동/수동 스케줄링으로 단어/블록 읽기/쓰기를 수행한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Port | 시리얼 포트 이름 (예: "COM1") | — |
| int | Baudrate | 통신 속도 (bps) | — |
| Parity | Parity | 패리티 설정 | — |
| int | DataBits | 데이터 비트 수 | — |
| StopBits | StopBits | 정지 비트 | — |
| int | Timeout | 응답 대기 시간 (ms) | 100 |
| int | Interval | 메시지 전송 간격 (ms) | 10 |
| int | BufferSize | 수신 버퍼 크기 (bytes) | 1024 |
| bool | IsOpen | 시리얼 포트 열림 여부 (get) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | AutoReconnect | 포트 닫힘 시 자동 재연결 여부 | — |
| bool | IsDisposed | Dispose 호출 여부 (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods -- 제어

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | Dispose | () | 리소스 해제 |
| bool | ContainAutoID | (int MessageID) | 자동 메시지 ID 존재 여부 확인 |
| bool | RemoveManual | (int MessageID) | 수동 메시지 제거 |
| bool | RemoveAuto | (int MessageID) | 자동 메시지 제거 |
| void | ClearManual | () | 모든 수동 메시지 삭제 |
| void | ClearAuto | () | 모든 자동 메시지 삭제 |
| void | ClearWorkSchedule | () | 작업 스케줄 전체 삭제 |

### Methods -- 자동 읽기 (Auto Read)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | AutoRSS | (int id, int slave, string device, int? timeout = null) | 단일 디바이스 자동 읽기 등록 |
| void | AutoRSS | (int id, int slave, string[] devices, int? timeout = null) | 복수 디바이스 자동 읽기 등록 |
| void | AutoRSB | (int id, int slave, string device, int length, int? timeout = null) | 블록 자동 읽기 등록 |

### Methods -- 수동 읽기 (Manual Read)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | ManualRSS | (int id, int slave, string device, int? repeatCount = null, int? timeout = null) | 단일 디바이스 수동 읽기 |
| void | ManualRSS | (int id, int slave, string[] devices, int? repeatCount = null, int? timeout = null) | 복수 디바이스 수동 읽기 |
| void | ManualRSB | (int id, int slave, string device, int length, int? repeatCount = null, int? timeout = null) | 블록 수동 읽기 |

### Methods -- 수동 쓰기 (Manual Write)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | ManualWSS | (int id, int slave, string device, int value, int? repeatCount = null, int? timeout = null) | 단일 디바이스 수동 쓰기 |
| void | ManualWSS | (int id, int slave, IEnumerable&lt;CNetValue&gt; values, int? repeatCount = null, int? timeout = null) | 복수 디바이스 수동 쓰기 |
| void | ManualWSB | (int id, int slave, string device, int[] values, int? repeatCount = null, int? timeout = null) | 블록 수동 쓰기 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;DataReadEventArgs&gt; | DataReceived | 읽기 응답 수신 시 발생 |
| EventHandler&lt;WriteEventArgs&gt; | WriteResponseReceived | 쓰기 응답 수신 시 발생 |
| EventHandler&lt;TimeoutEventArgs&gt; | TimeoutReceived | 응답 타임아웃 발생 시 |
| EventHandler&lt;BCCErrorEventArgs&gt; | BCCErrorReceived | BCC 체크섬 오류 시 |
| EventHandler&lt;NAKEventArgs&gt; | NAKReceived | NAK 응답 수신 시 (NAKEventArgs.ErrorCode에 오류 코드) |
| EventHandler | DeviceOpened | 포트 열림 시 |
| EventHandler | DeviceClosed | 포트 닫힘 시 |

---

## DataReadEventArgs

`public class DataReadEventArgs : EventArgs`

읽기 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| CNetFunc | Function | 함수 코드 (get) | — |
| int[] | Data | 수신 데이터 배열 (get) | — |
| string[] | ReadAddress | 읽기 주소 배열 (get) | — |

---

## WriteEventArgs

`public class WriteEventArgs : EventArgs`

쓰기 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| CNetFunc | Function | 함수 코드 (get) | — |

---

## TimeoutEventArgs

`public class TimeoutEventArgs : EventArgs`

타임아웃 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| CNetFunc | Function | 함수 코드 (get) | — |

---

## BCCErrorEventArgs

`public class BCCErrorEventArgs : EventArgs`

BCC 체크섬 오류 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| CNetFunc | Function | 함수 코드 (get) | — |

---

## NAKEventArgs

`public class NAKEventArgs : EventArgs`

NAK 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| CNetFunc | Function | 함수 코드 (get) | — |
| int | ErrorCode | 오류 코드 (get) | — |

---

## 간단 사용 예

```csharp
var cnet = new CNet { Port = "COM1", Baudrate = 9600 };
cnet.AutoRSB("%MW100", 10, 200);   // %MW100~109 자동 읽기, 200ms 주기
cnet.DataReceived += (s, e) => { var values = e.Values; };
cnet.Start();
cnet.ManualWSS("%MW200", new int[] { 100 });  // 쓰기
```
