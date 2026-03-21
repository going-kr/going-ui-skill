using Going.Basis.Communications;

namespace TemperatureMonitor
{
    public class DeviceManager
    {
        public MasterTCP TCP { get; } = new MasterTCP();
        public SensorData Data { get; private set; }

        public DeviceManager()
        {
            // 영역 매핑
            TCP.WordAreas.Add(0x0000, "D");

            // DeviceData 패턴
            Data = new SensorData(TCP, 1);
        }

        // 통신 상태
        public bool IsConnected => TCP.IsOpen;

        public void Start()
        {
            var setting = Main.DataMgr.Setting;
            TCP.RemoteIP = setting.RemoteIP;
            TCP.RemotePort = setting.RemotePort;
            TCP.Timeout = setting.Timeout;

            // 주기 읽기 등록: D0~D10 (온도 10개 + 상태 1개)
            TCP.MonitorWord_F3(1, 0x0000, 11);

            TCP.Start();
        }

        public void Stop()
        {
            TCP.Stop();
        }
    }
}
