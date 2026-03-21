# Mitsubishi MC Protocol API Reference

네임스페이스 `Going.Basis.Communications.Mitsubishi` — Mitsubishi PLC MC 프로토콜 시리얼 통신.

---

## MCFunc (enum)

MC 통신 함수 코드.

| Name | Description |
|------|-------------|
| None | 없음 |
| BitRead | 비트 읽기 |
| WordRead | 워드 읽기 |
| BitWrite | 비트 쓰기 |
| WordWrite | 워드 쓰기 |

---

## MC

`public class MC`

Mitsubishi PLC MC 프로토콜(3E/4E 프레임) 시리얼 통신 클라이언트. 비트/워드 자동/수동 읽기/쓰기를 지원한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Port | 시리얼 포트 이름 | — |
| int | Baudrate | 통신 속도 (bps) | — |
| Parity | Parity | 패리티 | — |
| int | DataBits | 데이터 비트 | — |
| StopBits | StopBits | 정지 비트 | — |
| int | Timeout | 응답 대기 시간 (ms) | 100 |
| int | Interval | 메시지 전송 간격 (ms) | 10 |
| int | BufferSize | 수신 버퍼 크기 (bytes) | 1024 |
| bool | IsOpen | 포트 열림 여부 (get) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | AutoReconnect | 자동 재연결 | — |
| bool | IsDisposed | Dispose 여부 (get) | — |
| bool | UseControlSequence | 제어 시퀀스 사용 | false |
| bool | UseCheckSum | 체크섬 사용 | false |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods -- 제어

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | Dispose | () | 리소스 해제 |
| bool | ContainAutoID | (int MessageID) | 자동 메시지 ID 존재 여부 |
| bool | RemoveManual | (int MessageID) | 수동 메시지 제거 |
| bool | RemoveAuto | (int MessageID) | 자동 메시지 제거 |
| void | ClearManual | () | 수동 메시지 전체 삭제 |
| void | ClearAuto | () | 자동 메시지 전체 삭제 |
| void | ClearWorkSchedule | () | 작업 스케줄 전체 삭제 |

### Methods -- 자동 읽기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | AutoBitRead | (int id, int slave, string device, int length, int waitTime = 0, int? timeout = null) | 비트 자동 읽기 등록 |
| void | AutoWordRead | (int id, int slave, string device, int length, int waitTime = 0, int? timeout = null) | 워드 자동 읽기 등록 |

### Methods -- 수동 읽기/쓰기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | ManualBitRead | (int id, int slave, string device, int length, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 비트 수동 읽기 |
| void | ManualBitWrite | (int id, int slave, string device, bool value, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 비트 단일 수동 쓰기 |
| void | ManualBitWrite | (int id, int slave, string device, bool[] value, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 비트 배열 수동 쓰기 |
| void | ManualWordRead | (int id, int slave, string device, int length, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 워드 수동 읽기 |
| void | ManualWordWrite | (int id, int slave, string device, int value, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 워드 단일 수동 쓰기 |
| void | ManualWordWrite | (int id, int slave, string device, int[] value, int waitTime = 0, int? repeatCount = null, int? timeout = null) | 워드 배열 수동 쓰기 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;WordDataReadEventArgs&gt; | WordDataReceived | 워드 읽기 응답 수신 |
| EventHandler&lt;BitDataReadEventArgs&gt; | BitDataReceived | 비트 읽기 응답 수신 |
| EventHandler&lt;WriteEventArgs&gt; | WriteResponseReceived | 쓰기 응답 수신 |
| EventHandler&lt;TimeoutEventArgs&gt; | TimeoutReceived | 타임아웃 발생 |
| EventHandler&lt;CheckSumErrorEventArgs&gt; | CheckSumErrorReceived | 체크섬 오류 발생 |
| EventHandler&lt;NakErrorEventArgs&gt; | NakErrorReceived | NAK 오류 응답 수신 |
| EventHandler | DeviceOpened | 포트 열림 |
| EventHandler | DeviceClosed | 포트 닫힘 |

---

## WordDataReadEventArgs

`public class WordDataReadEventArgs : EventArgs`

워드 읽기 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |
| int[] | Data | 수신 워드 데이터 배열 (get) | — |

---

## BitDataReadEventArgs

`public class BitDataReadEventArgs : EventArgs`

비트 읽기 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |
| bool[] | Data | 수신 비트 데이터 배열 (get) | — |

---

## WriteEventArgs

`public class WriteEventArgs : EventArgs`

쓰기 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |

---

## TimeoutEventArgs

`public class TimeoutEventArgs : EventArgs`

타임아웃 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |

---

## CheckSumErrorEventArgs

`public class CheckSumErrorEventArgs : EventArgs`

체크섬 오류 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |

---

## NakErrorEventArgs

`public class NakErrorEventArgs : EventArgs`

NAK 오류 응답 이벤트 인수.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | MessageID | 메시지 ID (get) | — |
| int | Slave | 슬레이브 번호 (get) | — |
| MCFunc | Function | 함수 코드 (get) | — |

---

## 간단 사용 예

```csharp
var mc = new MC { IP = "192.168.0.10", Port = 5000 };
mc.AutoWordRead(0, 1, "D0", 10, 200);   // id=0, slave=1, D0~D9, 200ms 주기
mc.WordDataReceived += (s, e) => { var data = e.Data; };
mc.Start();
mc.ManualWordWrite(0, 1, "D100", new int[] { 50 });  // 쓰기
```
