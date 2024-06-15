from enum import Enum, auto


class RequestIdPlayer(Enum):
    PlayerHiPush = 10001
    PlayerInitPullReq = 10002
    PlayerInitPullResp = 10003
    PlayerInitPlayerCorePush = 10010
    PlayerCreatePlayerCorePullReq = 10011
    PlayerCreatePlayerCorePullResp = 10012
    PlayerDestroyPlayerCorePush = 10013
    PlayerPrepareAsyncPush = 10014
    PlayerStartPush = 10015
    PlayerStopPush = 10016
    PlayerPausePush = 10017
    PlayerResumePush = 10018
    PlayerSetAudioMutePush = 10019
    PlayerSeekToAsyncPush = 10020
    PlayerGetCurrentPositionMsPullReq = 10021
    PlayerGetCurrentPositionMsPullResp = 10022
    PlayerSetVideoSurfacePush = 10023
    PlayerSetAudioVolumePush = 10024
    PlayerSetDataSourcePush = 10025
    PlayerSetLoaderSourcePush = 10026
    PlayerSetRepeatPush = 10027
    PlayerResizePush = 10028
    PlayerSetPlaySpeedRatio = 10029
    PlayerInfoPush = 10030
    PlayerErrorPlayerPush = 10031
    PlayerVideoSizeChangedPush = 10032
    PlayerUnknown0Push = 10033
    PlayerStatePush = 10034
    PlayerUnknonw1Push = 10035
    PlayerUnknown2Push = 10036
    PlayerStartTaskProxyPush = 10050
    PlayerStartRequestProxyPush = 10051
    PlayerCloseRequestProxyPush = 10052
    PlayerPollingDatProxyPullReq = 10054


class RequestIdUtility(Enum):
    UtilityHiPush = 10001  # 是Utility启动发送的
    UtilityInitPullReq = 10002  # 初始化请求
    UtilityInitPullResp = 10003  # 回复创建的都是Shared类型的info, 但是调用了SwapMMMojoWriteInfoCallback, 所以回调的还是Pull
    UtilityResampleImagePullReq = 10010
    UtilityResampleImagePullResp = 10011
    UtilityDecodeImagePullReq = 10020
    UtilityDecodeImagePullResp = 10021
    UtilityPicQRScanPullReq = 10030  # 10030是点击OCR时(也是打开图片时)发送的请求, 参数是图片路径
    UtilityQRScanPullReq = 10031  # 10031是截图框选时发送的请求, 参数应该是某种编码后的图片数据
    UtilityQRScanPullResp = 10032  # 这两种请求的返回ID都是10032
    UtilityTextScanPushResp = 10040  # TextScan具体在扫什么不是很清楚 可能是用来判断图片上是否有文字


class MMMojoInfoMethod(Enum):
    kMMNone = 0
    kMMPush = auto()
    kMMPullReq = auto()
    kMMPullResp = auto()
    kMMShared = auto()


class MMMojoEnvironmentCallbackType(Enum):
    kMMUserData = 0
    kMMReadPush = auto()
    kMMReadPull = auto()
    kMMReadShared = auto()
    kMMRemoteConnect = auto()
    kMMRemoteDisconnect = auto()
    kMMRemoteProcessLaunched = auto()
    kMMRemoteProcessLaunchFailed = auto()
    kMMRemoteMojoError = auto()


class MMMojoEnvironmentInitParamType(Enum):
    kMMHostProcess = 0
    kMMLoopStartThread = auto()
    kMMExePath = auto()
    kMMLogPath = auto()
    kMMLogToStderr = auto()
    kMMAddNumMessagepipe = auto()
    kMMSetDisconnectHandlers = auto()
    kMMDisableDefaultPolicy = 1000
    kMMElevated = auto()
    kMMCompatible = auto()


__all__ = [
    'RequestIdPlayer',
    'RequestIdUtility',
    'MMMojoInfoMethod',
    'MMMojoEnvironmentCallbackType',
    'MMMojoEnvironmentInitParamType'
]
