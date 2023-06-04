import multiprocessing
import gps

def get_gps_data(shared_data):
    # GPSデータの取得
    gps_data = gps.get_gps()

    # 共有メモリにGPSデータを書き込む
    shared_data.value = gps_data

if __name__ == "__main__":
    # 共有メモリを作成
    shared_data = multiprocessing.Value('d', 0.0)  # 'd'はdouble型を指定
    key = ftok("shared_memory_key", ord('A'))
    # プロセスを作成し、GPSデータの取得と共有メモリへの書き込みを行う
    gps_process = multiprocessing.Process(target=get_gps_data, args=(shared_data,))
    gps_process.start()

    # ここからは他の処理を行う

    # 共有メモリからデータを読み取り、必要な処理を行う
    #gps_value = shared_data.value
    #perform_calculation_with_gps_value(gps_value)

    # 他の処理が終了したらGPSプロセスを終了する
    gps_process.terminate()
    gps_process.join()

#以下おまけ(不要)
print(gps.get_gps()[0])
