# Modbus API Reference

네임스페이스 `Going.Basis.Communications.Modbus` — Modbus RTU/TCP 마스터/슬레이브 통신 라이브러리.

저수준(ModbusRTUMaster, ModbusTCPMaster, ModbusRTUSlave, ModbusTCPSlave) 클래스와
고수준 래퍼(MasterRTU, MasterTCP, SlaveRTU, SlaveTCP) 클래스를 제공한다.

---

## ModbusFunction (enum)

Modbus 함수 코드.

| Name | Value | Description |
|------|-------|-------------|
| BITREAD_F1 | 1 | 코일 읽기 |
| BITREAD_F2 | 2 | 입력 비트 읽기 |
| WORDREAD_F3 | 3 | 보유 레지스터 읽기 |
| WORDREAD_F4 | 4 | 입력 레지스터 읽기 |
| BITWRITE_F5 | 5 | 단일 코일 쓰기 |
| WORDWRITE_F6 | 6 | 단일 레지스터 쓰기 |
| MULTIBITWRITE_F15 | 15 | 다중 코일 쓰기 |
| MULTIWORDWRITE_F16 | 16 | 다중 레지스터 쓰기 |
| WORDBITSET_F26 | 26 | 레지스터 내 비트 설정 |

---

## ModbusCRC

Modbus CRC-16 및 LRC 체크섬 계산 유틸리티.

### Static Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | GetCRC | (byte[] pby, int nSize, ref byte byFirstReturn, ref byte bySecondReturn) | 바이트 배열의 CRC-16 계산 |
| static void | GetCRC | (List&lt;byte&gt; pby, int startindex, int nSize, ref byte byFirstReturn, ref byte bySecondReturn) | 리스트의 CRC-16 계산 (오프셋 지정) |
| static void | GetLRC | (byte[] pby, int nSize, ref byte byFirstReturn, ref byte bySecondReturn) | LRC (ASCII 모드) 체크섬 계산 |

---

## ModbusRTUMaster

`public class ModbusRTUMaster : IDisposable`

Modbus RTU 마스터. FC1/2(비트읽기), FC3/4(워드읽기), FC5(비트쓰기), FC6(워드쓰기), FC15/16(다중쓰기), FC26(워드비트셋) 지원.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Port | 시리얼 포트 이름 | — |
| int | Baudrate | 통신 속도 (bps) | — |
| Parity | Parity | 패리티 설정 | — |
| int | DataBits | 데이터 비트 수 | — |
| StopBits | StopBits | 정지 비트 | — |
| int | Timeout | 응답 대기 시간 (ms) | 100 |
| int | Interval | 메시지 전송 간격 (ms) | 10 |
| int | BufferSize | 수신 버퍼 크기 (bytes) | 1024 |
| bool | IsOpen | 포트 열림 여부 (get) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | AutoReconnect | 자동 재연결 여부 | — |
| bool | IsDisposed | Dispose 호출 여부 (get) | — |
| string | ModuleId | 모듈 식별자 GUID (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods -- 제어

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | Dispose | () | 리소스 해제 |
| bool | ContainAutoID | (int MessageID) | 자동 메시지 ID 존재 확인 |
| bool | RemoveManual | (int MessageID) | 수동 메시지 ID로 삭제 |
| bool | RemoveAuto | (int MessageID) | 자동 메시지 ID로 삭제 |
| void | ClearManual | () | 수동 메시지 전체 삭제 |
| void | ClearAuto | () | 자동 메시지 전체 삭제 |
| void | ClearWorkSchedule | () | 작업 큐 전체 삭제 |

### Methods -- 자동 읽기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | AutoBitRead_FC1 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC1 코일 자동 읽기 등록 |
| void | AutoBitRead_FC2 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC2 입력 비트 자동 읽기 등록 |
| void | AutoWordRead_FC3 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC3 보유 레지스터 자동 읽기 등록 |
| void | AutoWordRead_FC4 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC4 입력 레지스터 자동 읽기 등록 |

### Methods -- 수동 읽기/쓰기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | ManualBitRead_FC1 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC1 수동 읽기 |
| void | ManualBitRead_FC2 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC2 수동 읽기 |
| void | ManualWordRead_FC3 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC3 수동 읽기 |
| void | ManualWordRead_FC4 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC4 수동 읽기 |
| void | ManualBitWrite_FC5 | (int id, int slave, int startAddr, bool value, int? repeatCount = null, int? timeout = null) | FC5 단일 코일 쓰기 |
| void | ManualWordWrite_FC6 | (int id, int slave, int startAddr, int value, int? repeatCount = null, int? timeout = null) | FC6 단일 레지스터 쓰기 |
| void | ManualMultiBitWrite_FC15 | (int id, int slave, int startAddr, bool[] values, int? repeatCount = null, int? timeout = null) | FC15 다중 코일 쓰기 |
| void | ManualMultiWordWrite_FC16 | (int id, int slave, int startAddr, int[] values, int? repeatCount = null, int? timeout = null) | FC16 다중 레지스터 쓰기 |
| void | ManualWordBitSet_FC26 | (int id, int slave, int startAddr, byte bitIndex, bool value, int? repeatCount = null, int? timeout = null) | FC26 레지스터 내 비트 설정 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;BitReadEventArgs&gt; | BitReadReceived | 비트 읽기 응답 수신 |
| EventHandler&lt;WordReadEventArgs&gt; | WordReadReceived | 워드 읽기 응답 수신 |
| EventHandler&lt;BitWriteEventArgs&gt; | BitWriteReceived | FC5 쓰기 응답 수신 |
| EventHandler&lt;WordWriteEventArgs&gt; | WordWriteReceived | FC6 쓰기 응답 수신 |
| EventHandler&lt;MultiBitWriteEventArgs&gt; | MultiBitWriteReceived | FC15 응답 수신 |
| EventHandler&lt;MultiWordWriteEventArgs&gt; | MultiWordWriteReceived | FC16 응답 수신 |
| EventHandler&lt;WordBitSetEventArgs&gt; | WordBitSetReceived | FC26 응답 수신 |
| EventHandler&lt;TimeoutEventArgs&gt; | TimeoutReceived | 타임아웃 발생 |
| EventHandler&lt;CRCErrorEventArgs&gt; | CRCErrorReceived | CRC 오류 발생 |
| EventHandler | DeviceOpened | 포트 열림 |
| EventHandler | DeviceClosed | 포트 닫힘 |

---

## ModbusTCPMaster

`public class ModbusTCPMaster : IDisposable`

Modbus TCP 마스터. ModbusRTUMaster와 동일한 FC를 TCP 소켓으로 지원한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | RemoteIP | 원격 호스트 IP | "127.0.0.1" |
| int | RemotePort | 원격 포트 | 502 |
| int | Timeout | 응답 대기 시간 (ms) | 100 |
| int | Interval | 메시지 전송 간격 (ms) | 10 |
| int | BufferSize | 수신 버퍼 크기 (bytes) | 1024 |
| bool | IsOpen | 소켓 연결 여부 (get) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | AutoReconnect | 소켓 자동 재연결 | true |
| bool | IsDisposed | Dispose 호출 여부 (get) | — |
| string | ModuleId | 모듈 식별자 GUID (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods -- 제어

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | Dispose | () | 리소스 해제 |
| bool | ContainAutoID | (int MessageID) | 자동 ID 존재 확인 |
| bool | RemoveManual | (int MessageID) | 수동 메시지 ID로 삭제 |
| bool | RemoveAuto | (int MessageID) | 자동 메시지 ID로 삭제 |
| void | ClearManual | () | 수동 메시지 전체 삭제 |
| void | ClearAuto | () | 자동 메시지 전체 삭제 |
| void | ClearWorkSchedule | () | 작업 큐 전체 삭제 |

### Methods -- 자동 읽기

ModbusRTUMaster와 동일한 시그니처:

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | AutoBitRead_FC1 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC1 코일 자동 읽기 |
| void | AutoBitRead_FC2 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC2 입력 비트 자동 읽기 |
| void | AutoWordRead_FC3 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC3 보유 레지스터 자동 읽기 |
| void | AutoWordRead_FC4 | (int id, int slave, int startAddr, int length, int? timeout = null) | FC4 입력 레지스터 자동 읽기 |

### Methods -- 수동 읽기/쓰기

ModbusRTUMaster와 동일한 시그니처:

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | ManualBitRead_FC1 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC1 수동 읽기 |
| void | ManualBitRead_FC2 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC2 수동 읽기 |
| void | ManualWordRead_FC3 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC3 수동 읽기 |
| void | ManualWordRead_FC4 | (int id, int slave, int startAddr, int length, int? repeatCount = null, int? timeout = null) | FC4 수동 읽기 |
| void | ManualBitWrite_FC5 | (int id, int slave, int startAddr, bool value, int? repeatCount = null, int? timeout = null) | FC5 단일 코일 쓰기 |
| void | ManualWordWrite_FC6 | (int id, int slave, int startAddr, int value, int? repeatCount = null, int? timeout = null) | FC6 단일 레지스터 쓰기 |
| void | ManualMultiBitWrite_FC15 | (int id, int slave, int startAddr, bool[] values, int? repeatCount = null, int? timeout = null) | FC15 다중 코일 쓰기 |
| void | ManualMultiWordWrite_FC16 | (int id, int slave, int startAddr, int[] values, int? repeatCount = null, int? timeout = null) | FC16 다중 레지스터 쓰기 |
| void | ManualWordBitSet_FC26 | (int id, int slave, int startAddr, byte bitIndex, bool value, int? repeatCount = null, int? timeout = null) | FC26 레지스터 내 비트 설정 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;BitReadEventArgs&gt; | BitReadReceived | 비트 읽기 응답 |
| EventHandler&lt;WordReadEventArgs&gt; | WordReadReceived | 워드 읽기 응답 |
| EventHandler&lt;BitWriteEventArgs&gt; | BitWriteReceived | FC5 쓰기 응답 |
| EventHandler&lt;WordWriteEventArgs&gt; | WordWriteReceived | FC6 쓰기 응답 |
| EventHandler&lt;MultiBitWriteEventArgs&gt; | MultiBitWriteReceived | FC15 응답 |
| EventHandler&lt;MultiWordWriteEventArgs&gt; | MultiWordWriteReceived | FC16 응답 |
| EventHandler&lt;WordBitSetEventArgs&gt; | WordBitSetReceived | FC26 응답 |
| EventHandler&lt;TimeoutEventArgs&gt; | TimeoutReceived | 타임아웃 |
| EventHandler&lt;EventArgs&gt; | SocketConnected | TCP 소켓 연결 성공 |
| EventHandler&lt;EventArgs&gt; | SocketDisconnected | TCP 소켓 연결 해제 |

---

## ModbusRTUSlave

`public class ModbusRTUSlave`

Modbus RTU 슬레이브. 마스터의 요청을 이벤트로 수신하고, ProcessXxx 정적 메서드로 응답 데이터를 채운다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Port | 시리얼 포트 | — |
| int | Baudrate | 통신 속도 | — |
| Parity | Parity | 패리티 | — |
| int | DataBits | 데이터 비트 | — |
| StopBits | StopBits | 정지 비트 | — |
| bool | IsOpen | 포트 열림 여부 (get) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| object? | Tag | 사용자 데이터 | null |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 슬레이브 시작 |
| void | Stop | () | 슬레이브 정지 |

### Static Methods -- 요청 처리

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | ProcessBitReads | (BitReadRequestArgs args, int BaseAddress, bool[] BaseArray) | 비트 읽기 요청 처리 (응답 데이터 채우기) |
| static void | ProcessWordReads | (WordReadRequestArgs args, int BaseAddress, int[] BaseArray) | 워드 읽기 요청 처리 |
| static void | ProcessBitWrite | (BitWriteRequestArgs args, int BaseAddress, bool[] BaseArray) | 비트 쓰기 요청 처리 |
| static void | ProcessWordWrite | (WordWriteRequestArgs args, int BaseAddress, int[] BaseArray) | 워드 쓰기 요청 처리 |
| static void | ProcessMultiBitWrite | (MultiBitWriteRequestArgs args, int BaseAddress, bool[] BaseArray) | 다중 비트 쓰기 요청 처리 |
| static void | ProcessMultiWordWrite | (MultiWordWriteRequestArgs args, int BaseAddress, int[] BaseArray) | 다중 워드 쓰기 요청 처리 |
| static void | ProcessWordBitSet | (WordBitSetRequestArgs args, int BaseAddress, int[] BaseArray) | 워드비트셋 요청 처리 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;BitReadRequestArgs&gt; | BitReadRequest | FC1/FC2 읽기 요청 수신 |
| EventHandler&lt;WordReadRequestArgs&gt; | WordReadRequest | FC3/FC4 읽기 요청 수신 |
| EventHandler&lt;BitWriteRequestArgs&gt; | BitWriteRequest | FC5 쓰기 요청 수신 |
| EventHandler&lt;WordWriteRequestArgs&gt; | WordWriteRequest | FC6 쓰기 요청 수신 |
| EventHandler&lt;MultiBitWriteRequestArgs&gt; | MultiBitWriteRequest | FC15 쓰기 요청 수신 |
| EventHandler&lt;MultiWordWriteRequestArgs&gt; | MultiWordWriteRequest | FC16 쓰기 요청 수신 |
| EventHandler&lt;WordBitSetRequestArgs&gt; | WordBitSetRequest | FC26 요청 수신 |
| EventHandler | DeviceOpened | 포트 열림 |
| EventHandler | DeviceClosed | 포트 닫힘 |

---

## ModbusTCPSlave

`public class ModbusTCPSlave`

Modbus TCP 슬레이브. 클라이언트 연결을 수신하고 요청을 이벤트로 전달한다. ProcessXxx 정적 메서드로 응답 데이터를 채운다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | LocalPort | 로컬 리스닝 포트 | 502 |
| bool | IsStart | 슬레이브 시작 여부 (get) | — |
| object? | Tag | 사용자 데이터 | null |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 슬레이브 시작 |
| void | Stop | () | 슬레이브 정지 |

### Static Methods -- 요청 처리

ModbusRTUSlave와 동일한 시그니처 (단, EventArgs 타입은 ModbusTCPSlave 네임스페이스 소속):

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | ProcessBitReads | (BitReadRequestArgs args, int BaseAddress, bool[] BaseArray) | 비트 읽기 요청 처리 |
| static void | ProcessWordReads | (WordReadRequestArgs args, int BaseAddress, int[] BaseArray) | 워드 읽기 요청 처리 |
| static void | ProcessBitWrite | (BitWriteRequestArgs args, int BaseAddress, bool[] BaseArray) | 비트 쓰기 요청 처리 |
| static void | ProcessWordWrite | (WordWriteRequestArgs args, int BaseAddress, int[] BaseArray) | 워드 쓰기 요청 처리 |
| static void | ProcessMultiBitWrite | (MultiBitWriteRequestArgs args, int BaseAddress, bool[] BaseArray) | 다중 비트 쓰기 요청 처리 |
| static void | ProcessMultiWordWrite | (MultiWordWriteRequestArgs args, int BaseAddress, int[] BaseArray) | 다중 워드 쓰기 요청 처리 |
| static void | ProcessWordBitSet | (WordBitSetRequestArgs args, int BaseAddress, int[] BaseArray) | 워드비트셋 요청 처리 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;BitReadRequestArgs&gt; | BitReadRequest | FC1/FC2 읽기 요청 수신 |
| EventHandler&lt;WordReadRequestArgs&gt; | WordReadRequest | FC3/FC4 읽기 요청 수신 |
| EventHandler&lt;BitWriteRequestArgs&gt; | BitWriteRequest | FC5 쓰기 요청 수신 |
| EventHandler&lt;WordWriteRequestArgs&gt; | WordWriteRequest | FC6 쓰기 요청 수신 |
| EventHandler&lt;MultiBitWriteRequestArgs&gt; | MultiBitWriteRequest | FC15 쓰기 요청 수신 |
| EventHandler&lt;MultiWordWriteRequestArgs&gt; | MultiWordWriteRequest | FC16 쓰기 요청 수신 |
| EventHandler&lt;WordBitSetRequestArgs&gt; | WordBitSetRequest | FC26 요청 수신 |
| EventHandler&lt;EventArgs&gt; | SocketConnected | 클라이언트 연결 수신 |
| EventHandler&lt;EventArgs&gt; | SocketDisconnected | 클라이언트 연결 해제 |

---

## MasterRTU (래퍼)

`public class MasterRTU`

단순화된 Modbus RTU 마스터. 모니터링을 설정한 뒤 Dictionary 기반으로 최신값을 조회한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Port | 시리얼 포트 | — |
| int | Baudrate | 통신 속도 | — |
| Parity | Parity | 패리티 | — |
| int | DataBits | 데이터 비트 | — |
| StopBits | StopBits | 정지 비트 | — |
| int | Interval | 폴링 간격 (ms) | — |
| int | Timeout | 타임아웃 (ms) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | IsOpen | 포트 열림 여부 (get) | — |
| Dictionary&lt;int, string&gt; | BitAreas | 비트 영역 매핑 (baseAddr -> 코드 접두사) (get) | — |
| Dictionary&lt;int, string&gt; | WordAreas | 워드 영역 매핑 (baseAddr -> 코드 접두사) (get) | — |
| Dictionary&lt;int, Mems&gt; | Devices | 슬레이브별 비트/워드 최신값 저장소 (get) | — |
| Dictionary&lt;int, DateTime&gt; | LastReceived | 슬레이브별 최종 수신 시간 (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | MonitorBit_F1 | (int slave, int startAddr, int length) | FC1 코일 모니터링 등록 |
| void | MonitorBit_F2 | (int slave, int startAddr, int length) | FC2 입력 비트 모니터링 등록 |
| void | MonitorWord_F3 | (int slave, int startAddr, int length) | FC3 보유 레지스터 모니터링 등록 |
| void | MonitorWord_F4 | (int slave, int startAddr, int length) | FC4 입력 레지스터 모니터링 등록 |
| void | SetWord | (int slave, string addr, int value) | 워드 주소에 값 쓰기 |
| void | SetBit | (int slave, string addr, bool value) | 비트 주소에 값 쓰기 |
| int? | GetWord | (int slave, string addr) | 워드 주소 값 읽기 |
| bool? | GetBit | (int slave, string addr) | 비트 주소 값 읽기 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler | DeviceOpened | 포트 열림 |
| EventHandler | DeviceClosed | 포트 닫힘 |

---

## MasterTCP (래퍼)

`public class MasterTCP`

단순화된 Modbus TCP 마스터. MasterRTU의 TCP 버전으로, RemoteIP/RemotePort를 통해 연결한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | RemoteIP | 원격 서버 IP | — |
| int | RemotePort | 원격 서버 포트 | — |
| int | Interval | 폴링 간격 (ms) | — |
| int | Timeout | 타임아웃 (ms) | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | IsOpen | 소켓 연결 여부 (get) | — |
| Dictionary&lt;int, string&gt; | BitAreas | 비트 영역 매핑 (baseAddr -> 코드 접두사) (get) | — |
| Dictionary&lt;int, string&gt; | WordAreas | 워드 영역 매핑 (baseAddr -> 코드 접두사) (get) | — |
| Dictionary&lt;int, Mems&gt; | Devices | 슬레이브별 비트/워드 최신값 저장소 (get) | — |
| Dictionary&lt;int, DateTime&gt; | LastReceived | 슬레이브별 최종 수신 시간 (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods

MasterRTU와 동일한 시그니처:

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 통신 시작 |
| void | Stop | () | 통신 정지 |
| void | MonitorBit_F1 | (int slave, int startAddr, int length) | FC1 코일 모니터링 등록 |
| void | MonitorBit_F2 | (int slave, int startAddr, int length) | FC2 입력 비트 모니터링 등록 |
| void | MonitorWord_F3 | (int slave, int startAddr, int length) | FC3 보유 레지스터 모니터링 등록 |
| void | MonitorWord_F4 | (int slave, int startAddr, int length) | FC4 입력 레지스터 모니터링 등록 |
| void | SetWord | (int slave, string addr, int value) | 워드 주소에 값 쓰기 |
| void | SetBit | (int slave, string addr, bool value) | 비트 주소에 값 쓰기 |
| int? | GetWord | (int slave, string addr) | 워드 주소 값 읽기 |
| bool? | GetBit | (int slave, string addr) | 비트 주소 값 읽기 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;EventArgs&gt; | DeviceOpened | 소켓 연결 성공 |
| EventHandler&lt;EventArgs&gt; | DeviceClosed | 소켓 연결 해제 |

---

## SlaveRTU (래퍼)

`public class SlaveRTU`

단순화된 Modbus RTU 슬레이브. BitAreas/WordAreas Dictionary로 데이터 영역을 관리한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | Slave | 슬레이브 주소 | 1 |
| string | Port | 시리얼 포트 | — |
| int | Baudrate | 통신 속도 | — |
| Parity | Parity | 패리티 | — |
| int | DataBits | 데이터 비트 | — |
| StopBits | StopBits | 정지 비트 | — |
| bool | IsStart | 통신 시작 여부 (get) | — |
| bool | IsOpen | 포트 열림 여부 (get) | — |
| Dictionary&lt;int, BitMemory&gt; | BitAreas | 비트 데이터 영역 (baseAddr -> 메모리) (get) | — |
| Dictionary&lt;int, WordMemory&gt; | WordAreas | 워드 데이터 영역 (baseAddr -> 메모리) (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 슬레이브 시작 |
| void | Stop | () | 슬레이브 정지 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler | DeviceOpened | 포트 열림 |
| EventHandler | DeviceClosed | 포트 닫힘 |

---

## SlaveTCP (래퍼)

`public class SlaveTCP`

단순화된 Modbus TCP 슬레이브. LocalPort로 수신 대기한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| int | Slave | 슬레이브 주소 | 1 |
| int | LocalPort | 로컬 포트 | — |
| bool | IsStart | 슬레이브 시작 여부 (get) | — |
| Dictionary&lt;int, BitMemory&gt; | BitAreas | 비트 데이터 영역 (get) | — |
| Dictionary&lt;int, WordMemory&gt; | WordAreas | 워드 데이터 영역 (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 슬레이브 시작 |
| void | Stop | () | 슬레이브 정지 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;EventArgs&gt; | SocketConnected | 클라이언트 연결 수신 |
| EventHandler&lt;EventArgs&gt; | SocketDisconnected | 클라이언트 연결 해제 |

---

## Mems

`public class Mems`

MasterRTU/MasterTCP의 Devices에 저장되는 슬레이브 데이터 컨테이너.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| Dictionary&lt;string, bool&gt; | Bits | 비트 값 (주소문자열 -> 값) (get) | — |
| Dictionary&lt;string, int&gt; | Words | 워드 값 (주소문자열 -> 값) (get) | — |

---

## 간단 사용 예

> 패턴 기반 코드는 `comm-pattern.md` 참조. 아래는 API 시그니처 확인용 최소 예제.

### MasterRTU
```csharp
var rtu = new MasterRTU { Port = "COM1", Baudrate = 9600 };
rtu.WordAreas.Add(0x0000, "D");
rtu.MonitorWord_F3(1, 0x0000, 10);  // Slave 1, D0~D9
rtu.Start();
int? val = rtu.GetWord(1, "D0");
rtu.SetWord(1, "D5", 100);
```

### MasterTCP
```csharp
var tcp = new MasterTCP { RemoteIP = "192.168.0.10", RemotePort = 502 };
tcp.WordAreas.Add(0x0000, "D");
tcp.MonitorWord_F3(1, 0x0000, 10);
tcp.Start();
int? val = tcp.GetWord(1, "D0");
```
