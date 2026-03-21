# Tools & Utilities API Reference

네임스페이스 `Going.Basis.Tools` — 암호화, 수학, 네트워크, Windows 시스템 유틸리티.
네임스페이스 `Going.Basis.Utils` — 비동기 태스크, 외부 프로세스, 타이머, 정렬, 압축.
네임스페이스 `Going.Basis.Measure` — 채터링 제거 필터, 안정값 판정.

---

## CryptoTool

`public class CryptoTool`

Base64 인코딩/디코딩, AES-256/AES-128 암호화/복호화 유틸리티.

### Static Methods -- Base64

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static string? | EncodeBase64String | (string data, Encoding? enc = null) | 문자열을 Base64로 인코딩 |
| static string? | EncodeBase64String | (byte[] data) | 바이트 배열을 Base64로 인코딩 |
| static T? | DecodeBase64String&lt;T&gt; | (string data, Encoding? enc = null) | Base64를 지정 타입으로 역직렬화 |

### Static Methods -- AES-256

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static string | EncryptAES256 | (string input, string key, Encoding? enc = null) | AES-256 암호화 |
| static string | DecryptAES256 | (string input, string key, Encoding? enc = null) | AES-256 복호화 |

### Static Methods -- AES-128

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static string | EncryptAES128 | (string input, string key, Encoding? enc = null) | AES-128 암호화 |
| static string | DecryptAES128 | (string input, string key, Encoding? enc = null) | AES-128 복호화 |

---

## MathTool

`public static class MathTool`

값 범위 매핑, 제한, 각도/거리 계산, 사각형 생성, 점 변환 등 수학/기하 유틸리티.

### Static Methods -- 값 변환

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static long | Map | (long val, long min, long max, long convert_min, long convert_max) | 정수 범위 선형 매핑 |
| static double | Map | (double val, double min, double max, double convert_min, double convert_max) | 실수 범위 선형 매핑 |
| static T | Constrain&lt;T&gt; | (T val, T min, T max) | 값을 min~max 범위로 제한 (byte/short/int/long/float/double 등 지원) |

### Static Methods -- 기하

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static double | GetAngle | (Point from, Point to) | 두 점 사이 각도 (도) |
| static double | GetAngle | (PointF from, PointF to) | 두 점 사이 각도 (부동소수점) |
| static double | GetDistance | (Point a, Point b) | 두 점 사이 거리 |
| static double | GetDistance | (PointF a, PointF b) | 두 점 사이 거리 (부동소수점) |
| static double | GetDistance | (double x1, double y1, double z1, double x2, double y2, double z2) | 3D 두 점 사이 거리 |
| static double | GetDistance | (PointF LN1, PointF LN2, PointF pt) | 점에서 선분까지 거리 |
| static double | GetDistance | (double[] first, double[] second) | 배열 기반 유클리드 거리 |
| static PointF | RotatePoint | (PointF Center, PointF Target, float angle) | Center 기준으로 Target을 angle도 회전 |
| static int | StandardAngle | (int angle) | 각도를 0~360 범위로 정규화 (int) |
| static float | StandardAngle | (float angle) | 각도를 0~360 범위로 정규화 (float) |
| static double | StandardAngle | (double angle) | 각도를 0~360 범위로 정규화 (double) |
| static bool | CompareAngle | (double Angle, double StartAngle, double EndAngle) | 각도가 범위 내에 있는지 확인 |

### Static Methods -- 사각형/점

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static int/float | Center | (int/float p1, int/float p2) | 두 값의 중간값 |
| static int/float | CenterDist | (int/float x, int/float dist) | x 기준으로 dist 거리의 중심값 |
| static Point | CenterPoint | (Rectangle rt) | 사각형 중심점 |
| static PointF | CenterPoint | (RectangleF rt) | 사각형 중심점 (부동소수점) |
| static Point | CenterPoint | (Point p1, Point p2) | 두 점의 중심점 |
| static PointF | CenterPoint | (PointF p1, PointF p2) | 두 점의 중심점 (부동소수점) |
| static PointF[] | GetPoints | (RectangleF rt) | 사각형의 4개 꼭짓점 배열 반환 |
| static Rectangle/RectangleF | MakeRectangle | (여러 오버로드) | 두 점, 크기, 중심+크기 등으로 사각형 생성 (8+ 오버로드) |
| static PointF | GetPointWithAngle | (PointF p, float angle, float dist) | 원점에서 각도/거리로 점 계산 |
| static PointF | GetPointWithAngle | (Point p, float angle, float dist) | 원점에서 각도/거리로 점 계산 (Point) |
| static float | GetX_WithAngle | (PointF/Point p, float angle, float dist) | 각도/거리로 X 좌표 계산 (2개 오버로드) |
| static float | GetY_WithAngle | (PointF/Point p, float angle, float dist) | 각도/거리로 Y 좌표 계산 (2개 오버로드) |
| static float | LinearEquationY | (PointF p1, PointF p2, float x) | 두 점을 지나는 직선의 Y값 계산 |
| static float | LinearEquationX | (PointF p1, PointF p2, float y) | 두 점을 지나는 직선의 X값 계산 |

---

## NetworkTool

`public class NetworkTool`

IP 주소 유효성 검사, 로컬 IP 조회/설정, NIC 관리, 소켓 연결 확인.

### Static Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static bool | ValidIPv4 | (string address) | IPv4 주소 형식 유효성 검사 |
| static bool | ValidDomain | (string address) | 도메인 형식 유효성 검사 |
| static string | GetLocalIP | () | 현재 로컬 IP 주소 반환 |
| static bool | SetLocalIP | (string description, string ip, string subnet, string gateway) | NIC 고정 IP 설정 |
| static bool | SetDHCP | (string description) | NIC DHCP 설정 |
| static string[] | GetNicDescriptions | () | 설치된 NIC 설명 목록 반환 |
| static bool | IsSocketConnected | (Socket s, int PollTime = 100) | 소켓 연결 상태 확인 |

---

## WindowsTool

`public class WindowsTool`

Windows 시스템 시간 설정, 절전 방지/허용 유틸리티.

### Static Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | SetLocalTime | (DateTime Time) | Windows 로컬 시스템 시간 설정 |
| static void | SetSystemTime | (DateTime Time) | Windows UTC 시스템 시간 설정 |
| static void | PreventSleep | () | 디스플레이 절전 방지 (ES_DISPLAY_REQUIRED) |
| static void | AllowSleep | () | 절전 방지 해제 |

---

## EasyTask

`public class EasyTask`

비동기 반복 루프 태스크 관리. Started/Loop/Stopped 이벤트 기반으로 비동기 작업 라이프사이클을 관리한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| bool | IsStart | 태스크 실행 중 여부 (get) | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 태스크 시작 |
| void | Start | (CancellationToken cancellationToken) | 외부 취소 토큰으로 태스크 시작 |
| void | Stop | () | 태스크 정지 요청 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| Func&lt;CancellationToken, Task&gt; | Loop | 반복 실행할 비동기 루프 핸들러 |
| Func&lt;Task&gt; | Started | 태스크 시작 시 한 번 호출 |
| Func&lt;Task&gt; | Stopped | 태스크 종료 시 한 번 호출 |

---

## HiResTimer

`public class HiResTimer`

고해상도 타이머. System.Diagnostics.Stopwatch 기반으로 밀리초 단위 정밀 주기 타이머.

### Constructors

| Name | Parameters | Description |
|------|------------|-------------|
| HiResTimer | () | 기본 생성 |
| HiResTimer | (float interval) | 주기 지정 생성 (ms) |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| float | Interval | 타이머 주기 (ms) | — |
| float | IgnoreElapsedThreshold | 지연 무시 임계값. 이 값 초과 시 이벤트 건너뜀 | — |
| bool | Enabled | 타이머 활성 여부 | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 타이머 시작 |
| void | Stop | () | 타이머 정지 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;HiResTimerElapsedEventArgs&gt; | Elapsed | 주기마다 발생. HiResTimerElapsedEventArgs: Delay(실제 지연 ms), Fallouts(누락 횟수) |

---

## ExternalProgram

`public class ExternalProgram`

외부 프로세스 실행 및 종료 관리.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| ExternalProgram | (string PATH) | 실행 파일 경로로 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| Process? | Process | 실행 중인 프로세스 인스턴스 (get) | — |
| string | Path | 실행 파일 경로 (get) | — |
| string | ProcessName | 프로세스 이름 (get) | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Start | () | 프로세스 시작 |
| void | Stop | () | 프로세스 종료 |

---

## NaturalSortComparer

`public class NaturalSortComparer : IComparer<string>`

자연 정렬 비교자. 숫자 부분을 수치로 비교한다 ("item2" < "item10").

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| NaturalSortComparer | (bool ascending = true, bool ignoreCase = true, CultureInfo? culture = null) | 정렬 방향/대소문자 무시 여부 지정 |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| int | Compare | (string? x, string? y) | 두 문자열 자연 정렬 비교 |

---

## NaturalSortExtensions (static class)

`public static class NaturalSortExtensions`

자연 정렬 LINQ 확장 메서드.

### Static Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static IOrderedEnumerable&lt;TSource&gt; | OrderByNatural&lt;TSource&gt; | (this IEnumerable&lt;TSource&gt; source, Func&lt;TSource, string?&gt; keySelector, bool ascending = true, bool ignoreCase = true) | LINQ 자연 정렬 |
| static IOrderedEnumerable&lt;TSource&gt; | OrderByNaturalDescending&lt;TSource&gt; | (this IEnumerable&lt;TSource&gt; source, Func&lt;TSource, string?&gt; keySelector, bool ignoreCase = true) | LINQ 자연 역순 정렬 |
| static void | SortNatural&lt;T&gt; | (this List&lt;T&gt; list, Func&lt;T, string?&gt; keySelector, bool ascending = true) | List 인플레이스 자연 정렬 |

---

## CompressionUtility (static class)

`public static class CompressionUtility`

JSON 데이터 GZip 압축/해제 유틸리티. 데이터 크기가 임계값 이상일 때 자동 압축한다.

### Nested Classes

- **CompressionResult** -- 압축 결과. Properties: Data(string?), IsCompressed(bool), OriginalSize(int), ProcessedSize(int), CompressionRatio(double, 계산 프로퍼티)
- **DecompressionResult&lt;T&gt;** -- 해제 결과. Properties: Data(T?), WasCompressed(bool), OriginalSize(int), DecompressedSize(int)

### Static Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static CompressionResult | CompressJson&lt;T&gt; | (T obj) | 객체를 JSON 직렬화 후 GZip 압축 |
| static DecompressionResult&lt;T&gt; | DecompressJson&lt;T&gt; | (string base64Data, bool isCompressed, int originalSize) | Base64 데이터 해제 후 역직렬화 |
| static bool | ShouldCompress | (int dataSize) | 데이터 크기 기반 압축 여부 판단 |
| static string | GetCompressionInfo | (int originalSize, int processedSize, bool isCompressed) | 압축 결과 설명 문자열 |

---

## ChatteringMode (enum)

채터링 필터 적용 방향 설정.

| Name | Description |
|------|-------------|
| Both | ON/OFF 양방향 필터 |
| On | ON 방향만 필터 |
| Off | OFF 방향만 필터 |

---

## Chattering

`public class Chattering`

디지털 입력 신호의 채터링(튐) 제거 필터. 일정 시간 동안 안정적인 상태가 유지될 때만 상태 전이를 허용한다.

### Constructors

| Name | Parameters | Description |
|------|------------|-------------|
| Chattering | () | 기본 생성 (ChatteringTime=300ms, Mode=Both) |
| Chattering | (int chatteringTime) | 채터링 시간 지정 |
| Chattering | (int chatteringTime, ChatteringMode mode) | 시간 및 방향 지정 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| bool | State | 현재 필터링된 상태 (안정적으로 전이된 값) (get) | — |
| int | ChatteringTime | 채터링 판정 시간 (ms) | 300 |
| ChatteringMode | Mode | 필터 방향 모드 | Both |
| double | RemainingTime | 상태 전이까지 남은 시간 (ms) (get) | — |
| bool | CurrentInput | 현재 입력값 (필터링 전) (get) | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Set | (bool value) | 입력 신호 업데이트. 주기적으로 호출 필요 |
| void | Reset | (bool resetState = false) | 필터 초기화. resetState=true이면 State도 초기화 |
| string | GetStatus | () | 현재 상태 설명 문자열 반환 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;ChatteringStateChangedEventArgs&gt; | StateChanged | 상태 전이 시 발생. Value(새값), OldValue(이전값) |

---

## StableMode (enum)

안정값 판정 기준 모드.

| Name | Description |
|------|-------------|
| Absolute | 절댓값 기준 허용 오차 |
| Relative | 상대적 변화량 기준 (기본) |
| Hybrid | 절댓값 + 상대값 혼합 |

---

## Stable

`public class Stable`

아날로그 측정값이 ErrorRange 이내에서 MeasureTime 동안 유지되면 안정으로 판정한다. StableEventArgs로 안정화된 값을 전달한다.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| Stable | () | 기본 생성 (ErrorRange=1.0, MeasureTime=1000ms, Mode=Relative) |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| double | Value | 안정화 판정된 최신값 (get) | — |
| double | ErrorRange | 허용 오차 범위 | 1.0 |
| int | MeasureTime | 안정 판정 대기 시간 (ms) | 1000 |
| StableMode | Mode | 판정 기준 모드 | Relative |
| bool | IsStabilizing | 현재 안정화 측정 중 여부 (get) | — |
| double | CurrentReferenceValue | 현재 기준 참조값 (get) | — |
| double | RemainingTime | 안정 판정까지 남은 시간 (ms) (get) | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| void | Set | (double value) | 새 측정값 입력. 주기적으로 호출 필요 |
| void | Reset | () | 측정 상태 초기화 |
| string | GetStatus | () | 현재 상태 설명 문자열 |

### Events

| Signature | Name | Description |
|-----------|------|-------------|
| EventHandler&lt;StableEventArgs&gt; | Measured | 안정 판정 완료 시 발생. StableEventArgs.Value에 안정화된 값 |
| EventHandler&lt;StableEventArgs&gt; | Measuring | 측정 중 주기적으로 발생 |

---

## 간단 사용 예

### EasyTask
```csharp
EasyTask.Run("Polling", 1000, () => { /* 1초 주기 실행 */ });
EasyTask.Stop("Polling");
```

### HiResTimer
```csharp
var timer = new HiResTimer { Interval = 100 };
timer.Elapsed += (s, e) => { /* 100ms 주기 */ };
timer.Start();
```
