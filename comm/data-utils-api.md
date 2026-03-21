# Data Utilities API Reference

네임스페이스 `Going.Basis.Datas` — INI 파일, 직렬화 유틸리티.
네임스페이스 `Going.Basis.Memories` — 비트/워드 메모리.
네임스페이스 `Going.Basis.Extensions` — 정수형 비트/바이트 조작 확장 메서드.

---

## INI

`public class INI`

Windows INI 파일 읽기/쓰기 클래스.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| INI | (string Path) | INI 파일 경로로 인스턴스 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| string | Path | INI 파일 경로 (get) | — |

### Methods

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| bool | ExistsINI | () | INI 파일 존재 여부 확인 |
| void | Write | (string Section, string Key, string Value) | 키에 값 저장 |
| string | Read | (string Section, string Key) | 키 값 읽기 |
| void | DeleteSection | (string strSection) | 섹션 전체 삭제 |

---

## Serialize

`public class Serialize`

JSON, XML, Binary(구조체) 직렬화/역직렬화 정적 유틸리티 클래스.

### Static Methods -- JSON

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static string | JsonSerialize | (object obj, JsonSerializerOptions? options = null) | 객체를 JSON 문자열로 변환 |
| static string | JsonSerialize&lt;T&gt; | (T obj, JsonSerializerOptions? options = null) | 제네릭 버전 |
| static T? | JsonDeserialize&lt;T&gt; | (string? json, JsonSerializerOptions? options = null) | JSON 문자열을 객체로 역직렬화 |
| static void | JsonSerializeToFile | (string path, object obj, JsonSerializerOptions? options = null) | JSON을 파일로 저장 |
| static void | JsonSerializeToFile&lt;T&gt; | (string path, T obj, JsonSerializerOptions? options = null) | 제네릭 버전 |
| static T? | JsonDeserializeFromFile&lt;T&gt; | (string Path, JsonSerializerOptions? options = null) | JSON 파일을 객체로 역직렬화 |

### Static Methods -- XML

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | XmlSerializeToFile | (string Path, object obj, Type type) | XML 파일로 저장 |
| static object | XmlDeserializeFromFile | (string Path, Type type) | XML 파일에서 객체로 역직렬화 |
| static byte[] | XmlSerialize | (object obj, Type type) | 객체를 XML 바이트 배열로 직렬화 |
| static object | XmlDeserialize | (byte[] rawdata, Type type) | XML 바이트 배열에서 객체로 역직렬화 |

### Static Methods -- Raw (Binary/Struct)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static byte[] | RawSerialize | (object obj) | 구조체를 바이트 배열로 직렬화 |
| static object | RawDeserialize | (byte[] rawdata, Type type) | 바이트 배열에서 구조체로 역직렬화 |
| static object | RawDeserialize | (byte[] ba, int offset, int size, Type type) | 바이트 배열 부분 범위에서 구조체로 역직렬화 |
| static T | RawDeserialize&lt;T&gt; | (byte[] rawdata) where T : struct | 제네릭 구조체 역직렬화 |
| static T | RawDeserialize&lt;T&gt; | (byte[] ba, int offset, int size) | 제네릭 부분 범위 역직렬화 |

---

## IBitMemory (interface)

`public interface IBitMemory`

비트 메모리 인터페이스.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| bool | this[int index] | 인덱스로 비트 접근 (get set) | — |
| int | Count | 비트 수 (get) | — |
| byte[] | RawData | 원시 바이트 배열 (get) | — |

---

## IWordMemory (interface)

`public interface IWordMemory`

워드 메모리 인터페이스.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| WordRef | this[int index] | 인덱스로 WordRef 접근 (get) | — |
| int | Count | 워드 수 (get) | — |
| byte[] | RawData | 원시 바이트 배열 (get) | — |

---

## BitMemory

`public class BitMemory : IBitMemory`

비트 메모리 배열. bool 인덱서로 개별 비트에 접근한다. Modbus 슬레이브 데이터 영역에 사용된다. 경계 초과 시 get은 false를 반환하고 set은 무시한다.

### Constructors

| Name | Parameters | Description |
|------|------------|-------------|
| BitMemory | (int bitCount) | 비트 수로 초기화 (워드 단위 정렬) |
| BitMemory | (byte[] sharedRawData) | 외부 바이트 배열 공유 (복사 없음) |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| byte[] | RawData | 원시 바이트 배열 (get) | — |
| int | Count | 비트 수 (get) | — |
| bool | this[int index] | 인덱스로 비트 접근. 범위 초과 시 get=false, set=무시 (get set) | — |

---

## WordMemory

`public class WordMemory : IWordMemory`

워드 메모리 배열. WordRef 인덱서로 개별 워드에 접근한다. Modbus 슬레이브 레지스터 영역에 사용된다. 범위 초과 시 예외 발생.

### Constructors

| Name | Parameters | Description |
|------|------------|-------------|
| WordMemory | (int wordCount) | 워드 수로 초기화 |
| WordMemory | (byte[] sharedRawData) | 외부 바이트 배열 공유 (복사 없음) |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| WordRef | this[int index] | 인덱스로 WordRef 접근 (get) | — |
| int | Count | 워드 수 (get) | — |
| byte[] | RawData | 원시 바이트 배열 (get) | — |

---

## WordRef

`public class WordRef`

RawData 내 특정 오프셋의 워드를 다양한 타입으로 접근하는 래퍼.

### Constructor

| Name | Parameters | Description |
|------|------------|-------------|
| WordRef | (byte[] rawData, int byteOffset) | 바이트 배열과 오프셋으로 생성 |

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| ushort | W | 부호 없는 16비트 값 (0~65535) (get set) | — |
| short | IW | 부호 있는 16비트 값 (-32768~32767) (get set) | — |
| uint | DW | 32비트 더블워드 (현재+다음 워드, 4바이트) (get set) | — |
| int | IDW | 부호 있는 32비트 더블워드 (get set) | — |
| float | R | IEEE 754 실수 (4바이트) (get set) | — |
| string | S | UTF-8 문자열 (null 종단, 최대 256바이트) (get set) | — |
| byte | Byte0 | 하위 바이트 (get set) | — |
| byte | Byte1 | 상위 바이트 (get set) | — |
| BitAccessor | Bit | 16비트 비트 접근자 (Bit[0]~Bit[15]) (get) | — |

---

## BitAccessor

`public class BitAccessor`

WordRef 내 16비트 비트 접근자. 인덱서로 개별 비트 읽기/쓰기를 수행한다.

### Properties

| Type | Name | Description | Default |
|------|------|-------------|---------|
| bool | this[int index] | 비트 인덱스 0~15. 범위 초과 시 get=false, set=무시 (get set) | — |

---

## Bits (static class)

`public static class Bits`

네임스페이스 `Going.Basis.Extensions` -- byte, ushort, short, int, uint 타입에 비트/바이트 Get/Set 확장 메서드를 추가한다.

### GetBit -- 비트 읽기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static bool | GetBit | (this byte value, int bitIndex) | byte에서 지정 비트 읽기 |
| static bool | GetBit | (this ushort value, int bitIndex) | ushort에서 지정 비트 읽기 |
| static bool | GetBit | (this short value, int bitIndex) | short에서 지정 비트 읽기 |
| static bool | GetBit | (this int value, int bitIndex) | int에서 지정 비트 읽기 |
| static bool | GetBit | (this uint value, int bitIndex) | uint에서 지정 비트 읽기 |

### SetBit -- 비트 쓰기 (ref)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | SetBit | (this ref byte value, int bitIndex, bool bitValue) | byte의 지정 비트 설정 |
| static void | SetBit | (this ref ushort value, int bitIndex, bool bitValue) | ushort의 지정 비트 설정 |
| static void | SetBit | (this ref short value, int bitIndex, bool bitValue) | short의 지정 비트 설정 |
| static void | SetBit | (this ref int value, int bitIndex, bool bitValue) | int의 지정 비트 설정 |
| static void | SetBit | (this ref uint value, int bitIndex, bool bitValue) | uint의 지정 비트 설정 |

### GetByte -- 바이트 읽기

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static byte | GetByte | (this short value, int byteIndex) | short에서 바이트 추출 (byteIndex: 0=하위, 1=상위) |
| static byte | GetByte | (this ushort value, int byteIndex) | ushort에서 바이트 추출 |
| static byte | GetByte | (this int value, int byteIndex) | int에서 바이트 추출 (byteIndex: 0~3) |
| static byte | GetByte | (this uint value, int byteIndex) | uint에서 바이트 추출 |

### SetByte -- 바이트 쓰기 (ref)

| Return | Name | Parameters | Description |
|--------|------|------------|-------------|
| static void | SetByte | (this ref short value, int byteIndex, byte byteValue) | short의 지정 바이트 설정 |
| static void | SetByte | (this ref ushort value, int byteIndex, byte byteValue) | ushort의 지정 바이트 설정 |
| static void | SetByte | (this ref int value, int byteIndex, byte byteValue) | int의 지정 바이트 설정 |
| static void | SetByte | (this ref uint value, int byteIndex, byte byteValue) | uint의 지정 바이트 설정 |

---

## 간단 사용 예

### INI
```csharp
INI.Set("Config.ini", "Comm", "Port", "COM1");
string port = INI.Get("Config.ini", "Comm", "Port");
```

### Serialize
```csharp
Serialize.JsonSerializeToFile(setting, "setting.json");
var setting = Serialize.JsonDeserializeFromFile<Setting>("setting.json");
```
