using Going.Basis.Communications;

namespace TemperatureMonitor
{
    // DeviceData 패턴: 슬레이브 1대의 레지스터 의미를 래핑
    public class SensorData
    {
        public int ID { get; set; }             // 슬레이브 번호
        private MasterTCP Master { get; set; }

        public SensorData(MasterTCP master, int slaveId)
        {
            Master = master;
            ID = slaveId;
        }

        // 읽기 — GetWord로 래핑 (0.1℃ 단위 → double 변환)
        public double Temp0 => (Master.GetWord(ID, "D0") ?? 0) / 10.0;   // 온도 센서 1
        public double Temp1 => (Master.GetWord(ID, "D1") ?? 0) / 10.0;   // 온도 센서 2
        public double Temp2 => (Master.GetWord(ID, "D2") ?? 0) / 10.0;   // 온도 센서 3
        public double Temp3 => (Master.GetWord(ID, "D3") ?? 0) / 10.0;   // 온도 센서 4
        public double Temp4 => (Master.GetWord(ID, "D4") ?? 0) / 10.0;   // 온도 센서 5
        public double Temp5 => (Master.GetWord(ID, "D5") ?? 0) / 10.0;   // 온도 센서 6
        public double Temp6 => (Master.GetWord(ID, "D6") ?? 0) / 10.0;   // 온도 센서 7
        public double Temp7 => (Master.GetWord(ID, "D7") ?? 0) / 10.0;   // 온도 센서 8
        public double Temp8 => (Master.GetWord(ID, "D8") ?? 0) / 10.0;   // 온도 센서 9
        public double Temp9 => (Master.GetWord(ID, "D9") ?? 0) / 10.0;   // 온도 센서 10

        // 상태 비트 (D10)
        private int StatusBits => Master.GetWord(ID, "D10") ?? 0;
        public bool IsRunning  => (StatusBits & 0x01) != 0;  // bit0: Run
        public bool IsAlarm    => (StatusBits & 0x02) != 0;  // bit1: Alarm
        public bool IsOverTemp => (StatusBits & 0x04) != 0;  // bit2: OverTemp

        // 온도 배열 접근 (인덱서)
        public double GetTemp(int index) => index switch
        {
            0 => Temp0, 1 => Temp1, 2 => Temp2, 3 => Temp3, 4 => Temp4,
            5 => Temp5, 6 => Temp6, 7 => Temp7, 8 => Temp8, 9 => Temp9,
            _ => 0
        };
    }
}
