# MQTT API Reference

네임스페이스 `Going.Basis.Communications.Mqtt` — MQTT 브로커 Publish/Subscribe 클라이언트.

---

## MQQos (enum)

MQTT QoS(Quality of Service) 수준.

| Name | Description |
|------|-------------|
| MostOnce | 최대 1회 전달 (기본) |
| LeastOnce | 최소 1회 전달 |
| ExactlyOnce | 정확히 1회 전달 |
| GrantedFailure | 구독 실패 |

---

## MQSubscribe

`public class MQSubscribe`

MQTT 토픽 구독 정보를 담는 데이터 클래스.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| MQSubscribe | (string topic, MQQos qos = MQQos.MostOnce) | 토픽과 QoS로 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Topic | 구독할 MQTT 토픽 (get) | — |
| MQQos | Qos | QoS 수준 (get) | MostOnce |

---

## MQReceiveArgs

`public class MQReceiveArgs : EventArgs`

메시지 수신 이벤트 인수.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| MQReceiveArgs | (string Topic, byte[] Datas) | 토픽과 페이로드로 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Topic | 수신된 메시지의 토픽 (get) | — |
| byte[] | Datas | 수신된 페이로드 바이트 배열 (get) | — |

---

## MQClient

`public class MQClient`

MQTT 브로커에 연결하여 메시지를 발행(Publish)하고 구독(Subscribe)하는 클라이언트.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | BrokerHostName | 브로커 호스트명 또는 IP | "127.0.0.1" |
| bool | IsStart | 클라이언트 시작 여부 (get) | — |
| bool | IsConnected | 브로커 연결 여부 (get) | — |
| string? | ClientID | MQTT 클라이언트 ID (get) | — |
| string? | UserName | 인증 사용자명 (get) | — |
| string? | Password | 인증 비밀번호 (get) | — |
| List&lt;MQSubscribe&gt; | Subscribes | 현재 구독 목록 (get) | — |
| object? | Tag | 사용자 정의 데이터 | null |

### Methods -- 연결

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 브로커 연결 시작 (익명) |
| void | Start | (string? clientID) | 클라이언트 ID 지정 후 연결 |
| void | Start | (string? clientID, string? userName, string? password) | 인증 정보 지정 후 연결 |
| void | Stop | () | 연결 종료 |
| static bool | Test | (string BrokerIP, string ClientID) | 브로커 연결 가능 여부 테스트 |

### Methods -- Publish / Subscribe

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Publish | (string Topic, byte[] Data, MQQos qos = MostOnce, bool retain = false) | 바이트 페이로드 발행 |
| void | Publish | (string Topic, string Data, MQQos qos = MostOnce, bool retain = false) | 문자열 페이로드 발행 |
| void | Subscribe | (MQSubscribe sub) | MQSubscribe 객체로 구독 |
| void | Subscribe | (string Topic) | 토픽 문자열로 구독 (기본 QoS) |
| void | Subscribe | (string Topic, MQQos Qos) | QoS 지정 구독 |
| void | Unsubscribe | (string Topic) | 토픽 구독 해제 |
| void | UnsubscribeClear | () | 모든 구독 해제 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler | Connected | 브로커 연결 성공 시 |
| EventHandler | Disconnected | 브로커 연결 해제 시 |
| EventHandler&lt;MQReceiveArgs&gt; | Received | 구독 메시지 수신 시 (MQReceiveArgs.Topic, MQReceiveArgs.Datas) |

---

## 간단 사용 예

```csharp
var mqtt = new MQClient { BrokerHostName = "192.168.0.100" };
mqtt.Subscribe(new MQSubscribe("sensor/temp", MQQos.AtLeastOnce));
mqtt.Received += (s, e) => { var data = e.Datas; };
mqtt.Start("clientId");
mqtt.Publish("cmd/start", "1", MQQos.AtLeastOnce);
```
