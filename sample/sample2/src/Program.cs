using TemperatureMonitor;

var dataMgr = Main.DataMgr = new DataManager();
dataMgr.Load();

var devMgr = Main.DevMgr = new DeviceManager();
var wnd = Main.Window = new MainWindow();

devMgr.Start();
wnd.Run();
devMgr.Stop();

wnd.Dispose();
