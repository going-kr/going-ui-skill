# Going UI — 트러블슈팅 가이드

증상별 원인과 해결 방법. 에러 발생 시 이 파일을 `Read`로 읽고 해당 증상을 찾을 것.

---

## 빌드 에러

| 증상 (에러 메시지/로그) | 원인 | 해결 |
|------|------|------|
| `FileNotFoundException: design.json` 또는 `Could not find file 'design.json'` | UIEditor에서 MakeCode 미실행, 또는 design.json이 `bin/` 출력 디렉터리에 없음 | UIEditor에서 MakeCode 실행. csproj에 `<Content Include="design.json"><CopyToOutputDirectory>Always</CopyToOutputDirectory></Content>` 추가 |
| `NullReferenceException` in `*.Designer.cs` (예: `tbl.Controls["btn1"]` → null) | .gud에서 컨트롤 Name을 변경했으나 Designer.cs를 재생성하지 않음 | **Designer.cs 직접 수정 금지** — UIEditor에서 .gud 열고 MakeCode 재실행 |
| `JsonException` in `GoDesign.JsonDeserialize` — `The JSON value could not be converted` | design.json이 수동 편집으로 손상되었거나 라이브러리 버전과 불일치 | design.json 직접 수정 금지. UIEditor에서 .gud 다시 열고 MakeCode 재실행 |
| `NU1605` / `Version conflict detected for Going.UI` | Going.UI와 Going.UI.OpenTK 버전이 다름 | csproj에서 두 패키지 버전을 동일하게 통일 |
| `CS0246: The type or namespace 'GoInputNumber<>' could not be found` | `using Going.UI.Controls;` 누락 또는 제네릭 타입명이 C# alias가 아닌 .NET 타입명 사용 | Designer.cs의 타입 선언 확인: `GoInputNumber<Int32>` (int 아님), `GoValueNumber<Double>` (double 아님) |

## 통신 에러

| 증상 (코드 상태/로그) | 원인 | 해결 |
|------|------|------|
| `RTU.IsOpen == false`가 `Start()` 후에도 유지 | 시리얼 포트명 오류(`"COM1"` vs `"/dev/ttyUSB0"`), 포트 권한 부족, USB 케이블 미연결 | Linux: `ls /dev/ttyUSB*`로 포트 확인, `sudo chmod 666 /dev/ttyUSB0`. Windows: 장치 관리자에서 COM 포트 확인 |
| `TimeoutReceived` 이벤트만 반복 발생, `DataReceived` 없음 | Baudrate/Parity/StopBits 불일치, 슬레이브 번호 오류, 주소 범위 초과 | PLC 측 설정과 대조: `RTU.Baudrate`, `RTU.Parity`, `RTU.StopBits` 일치 확인. `MonitorWord_F3(slave, addr, len)`의 slave/addr이 PLC 설정과 동일한지 확인 |
| MQTT `Disconnected` 이벤트 반복 | 브로커 IP 오류, 방화벽, ClientID 중복 (동일 ID로 2개 연결 시 킥) | `mqtt.BrokerHostName` 확인. `ping {broker_ip}` 테스트. ClientID를 `$"client_{Guid.NewGuid():N}"` 등 고유값 사용 |
| CNet/MC `NAKReceived` 또는 `NakErrorReceived` 반복 | PLC 디바이스 주소 문자열 형식 오류 (예: `"D100"` vs `"%MW100"`) | CNet은 LS 주소체계(`"%MW100"`), MC는 Mitsubishi 주소체계(`"D0"`) 사용. API 문서에서 디바이스 주소 형식 확인 |

## 런타임 에러

| 증상 (화면/동작) | 원인 | 해결 |
|------|------|------|
| 앱 실행 시 빈 화면 (검은색/흰색만 표시) | `design.Init(this)` 미호출 또는 design.json 파싱 실패 | MainWindow 생성자에서 `design = GoDesign.JsonDeserialize(File.ReadAllText("design.json"))` → `design.Init(this)` 호출 순서 확인 |
| 버튼 클릭해도 이벤트 핸들러 미실행 | Designer.cs의 컨트롤 Name(`tbl.Controls["btnStart"]`)과 코드의 이벤트 바인딩 대상이 불일치 | Designer.cs에서 `var btnStart = ...` 변수명 확인 후, 코드에서 동일한 변수에 `+= (o, s) => { }` 바인딩 |
| GoInputText 탭 시 키패드 미출현 | `Main.Window.Keypad`가 null이거나, GoInputText의 `ReadOnly = true` | MainWindow에서 `Keypad = new GoKeypad()` 초기화 확인. 해당 컨트롤의 `ReadOnly` 속성 확인 |
| `InvalidOperationException: Collection was modified` in OnUpdate | OnUpdate에서 ObservableList에 직접 Add/Remove 중 렌더링과 충돌 | UI 스레드에서만 컬렉션 수정. 통신 스레드에서 값 변경 시 `design.Invoke(() => list.Add(item))` 사용 |

## 배포 에러 (gtcli)

| 증상 (gtcli 출력/동작) | 원인 | 해결 |
|------|------|------|
| `401 Unauthorized` 또는 `Authentication failed` | MCP 토큰이 틀리거나 만료됨 | 장치 웹 UI(http://{host}:5000)에서 토큰 재확인. `--token` 옵션에 정확한 값 전달 |
| `Connection refused` 또는 타임아웃 | 장치 IP 오류, MCP 서버(포트 5001) 미실행, 방화벽 차단 | `gtcli scan`으로 장치 IP 확인. `ping {host}` 테스트. 장치 웹 UI(포트 5000) 접속 가능한지 확인 |
| deploy 성공하지만 앱 미시작 | `executableFileName` 파라미터가 실제 실행 파일명과 불일치 | `dotnet publish` 출력에서 실행 파일명 확인. csproj의 `<AssemblyName>` 과 일치해야 함 |
| `File not found` 또는 zip 관련 에러 | zip 파일 경로 오류, 또는 zip 내부에 실행 파일이 루트에 없음 | zip 내부 구조 확인: 실행 파일이 zip 루트에 있어야 함 (`publish/` 하위가 아닌 `publish` 내용물 직접 압축) |
