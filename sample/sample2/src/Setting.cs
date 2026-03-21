namespace TemperatureMonitor
{
    public class Setting
    {
        public string RemoteIP { get; set; } = "192.168.0.100";
        public int RemotePort { get; set; } = 502;
        public int Timeout { get; set; } = 1000;
    }
}
