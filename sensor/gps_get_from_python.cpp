#include <iostream>
#include <sys/ipc.h>
#include <sys/shm.h>

/*
int main() {
    // 共有メモリのキーを指定してアクセスする
    key_t key = ftok("shared_memory_key", 1234);
    int shmid = shmget(key, sizeof(double), 0666);
    if (shmid == -1) {
        std::cerr << "Failed to access shared memory." << std::endl;
        return 1;
    }
*/
int main(int argc, char *argv[])
{
    if (argc < 1)
    {
        std::cerr << "GPS value is missing." << std::endl;
        return 1;
    }

    // GPSの値を取得
    const char*gpsData = argv[1];

    // GPSの値を表示
    std::cout << "GPS Data: " << *gpsData << std::endl;

    // 以降のコードでGPSの値を使用する

    return 0;
}

/*
    // 共有メモリをアタッチし、データを読み取る
    void* shared_memory = shmat(shmid, nullptr, 0);
    if (shared_memory == (void*)-1) {
        std::cerr << "Failed to attach shared memory." << std::endl;
        return 1;
    }

    double* gps_data = static_cast<double*>(shared_memory);
    std::cout << "GPS data: " << *gps_data << std::endl;

    // 共有メモリをデタッチする
    shmdt(shared_memory);

    return 0;
}
*/

