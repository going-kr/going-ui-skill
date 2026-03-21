using Going.Basis.Datas;

namespace TemperatureMonitor
{
    public class DataManager
    {
        private const string SettingFile = "setting.json";

        public Setting Setting { get; set; } = new Setting();

        public void Load()
        {
            if (File.Exists(SettingFile))
                Setting = Serialize.JsonDeserializeFromFile<Setting>(SettingFile) ?? new Setting();
        }

        public void Save()
        {
            Serialize.JsonSerializeToFile(Setting, SettingFile);
        }
    }
}
