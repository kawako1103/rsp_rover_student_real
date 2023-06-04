import subprocess
import gps

#GPSの値を取得する処理（仮定）
#gps_value = "35.12345, 139.67890"
gps_value = char(gps.get_gps())

#C++の実行ファイルを呼び出し、GPSの値を渡す
subprocess.call(["./gps_get_from_python", gps_value])
