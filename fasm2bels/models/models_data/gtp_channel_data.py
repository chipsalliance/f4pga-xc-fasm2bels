params = {
    "ACJTAG_RESET": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "ACJTAG_DEBUG_MODE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "ACJTAG_MODE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "UCODEER_CLR": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXBUFRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXCDRPHRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXCDRFREQRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXPMARESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXPCSRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXLPMRESET_TIME": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "RXISCANRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXSYNC_OVRD": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXSYNC_OVRD": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXSYNC_SKIP_DA": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXSYNC_SKIP_DA": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXSYNC_MULTILANE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXSYNC_MULTILANE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPCSRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "TXPMARESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RX_XCLK_SEL": {
        "type": "STR",
        "values": ["RXREC", "RXUSR"],
        "digits": 1
    },
    "RX_DATA_WIDTH": {
        "type": "INT",
        "values": [16, 20, 32, 40],
        "encoding": [2, 3, 4, 5],
        "digits": 3
    },
    "RX_CLK25_DIV": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        ],
        "digits":
        5
    },
    "RX_CM_SEL": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "RXPRBS_ERR_LOOPBACK": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "SATA_BURST_SEQ_LEN": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "OUTREFCLK_SEL_INV": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "SATA_BURST_VAL": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "RXOOB_CFG": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "SAS_MIN_COM": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "SATA_MIN_BURST": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61
        ],
        "digits":
        6
    },
    "SATA_EIDLE_VAL": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "SATA_MIN_WAKE": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "SATA_MIN_INIT": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "SAS_MAX_COM": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
            88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103,
            104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
            117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
            88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103,
            104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
            117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127
        ],
        "digits":
        7
    },
    "SATA_MAX_BURST": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "SATA_MAX_WAKE": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "SATA_MAX_INIT": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "RXOSCALRESET_TIMEOUT": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXOSCALRESET_TIME": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "TRANS_TIME_RATE": {
        "type": "BIN",
        "values": [255],
        "digits": 8
    },
    "PMA_LOOPBACK_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TX_PREDRIVER_MODE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TX_EIDLE_DEASSERT_DELAY": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TX_EIDLE_ASSERT_DELAY": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TX_LOOPBACK_DRIVE_HIZ": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TX_DRIVE_MODE": {
        "type": "STR",
        "values": ["DIRECT", "PIPE"],
        "digits": 1
    },
    "PD_TRANS_TIME_TO_P2": {
        "type": "BIN",
        "values": [255],
        "digits": 8
    },
    "PD_TRANS_TIME_NONE_P2": {
        "type": "BIN",
        "values": [255],
        "digits": 8
    },
    "PD_TRANS_TIME_FROM_P2": {
        "type": "BIN",
        "values": [4095],
        "digits": 12
    },
    "PCS_PCIE_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TXBUF_RESET_ON_RATE_CHANGE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TXBUF_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TXGEARBOX_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "GEARBOX_MODE": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "RXLPM_HOLD_DURING_EIDLE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RX_OS_CFG": {
        "type": "BIN",
        "values": [8191],
        "digits": 13
    },
    "RXLPM_LF_CFG": {
        "type": "BIN",
        "values": [262144],
        "digits": 18
    },
    "RXLPM_HF_CFG": {
        "type": "BIN",
        "values": [16383],
        "digits": 14
    },
    "ES_QUALIFIER": {
        "type": "BIN",
        "values": [1208833588708967444709375],
        "digits": 80
    },
    "ES_QUAL_MASK": {
        "type": "BIN",
        "values": [1208833588708967444709375],
        "digits": 80
    },
    "ES_SDATA_MASK": {
        "type": "BIN",
        "values": [1208833588708967444709375],
        "digits": 80
    },
    "ES_PRESCALE": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "ES_VERT_OFFSET": {
        "type": "BIN",
        "values": [511],
        "digits": 9
    },
    "ES_HORZ_OFFSET": {
        "type": "BIN",
        "values": [4095],
        "digits": 12
    },
    "RX_DISPERR_SEQ_MATCH": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "DEC_PCOMMA_DETECT": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "DEC_MCOMMA_DETECT": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "DEC_VALID_COMMA_ONLY": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "ES_ERRDET_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "ES_EYE_SCAN_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "ES_CONTROL": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "ALIGN_COMMA_ENABLE": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "ALIGN_MCOMMA_VALUE": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "RXSLIDE_MODE": {
        "type": "STR",
        "values": ["OFF", "AUTO", "PCS", "PMA"],
        "digits": 2
    },
    "ALIGN_PCOMMA_VALUE": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "ALIGN_COMMA_WORD": {
        "type": "INT",
        "values": [1, 2],
        "encoding": [1, 2],
        "digits": 2
    },
    "RX_SIG_VALID_DLY": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        ],
        "digits":
        5
    },
    "ALIGN_PCOMMA_DET": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "ALIGN_MCOMMA_DET": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "SHOW_REALIGN_COMMA": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "ALIGN_COMMA_DOUBLE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXSLIDE_AUTO_WAIT": {
        "type": "INT",
        "values": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "encoding": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "digits": 4
    },
    "CLK_CORRECT_USE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CLK_COR_SEQ_1_ENABLE": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "CLK_COR_SEQ_1_1": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_MAX_LAT": {
        "type":
        "INT",
        "values": [
            6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
            58, 59, 60
        ],
        "encoding": [
            6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
            58, 59, 60
        ],
        "digits":
        6
    },
    "CLK_COR_SEQ_1_2": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_MIN_LAT": {
        "type":
        "INT",
        "values": [
            4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60
        ],
        "encoding": [
            4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60
        ],
        "digits":
        6
    },
    "CLK_COR_SEQ_1_3": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_REPEAT_WAIT": {
        "type":
        "INT",
        "values": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        ],
        "digits":
        5
    },
    "CLK_COR_SEQ_1_4": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_SEQ_2_USE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CLK_COR_SEQ_2_ENABLE": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "CLK_COR_SEQ_2_1": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_KEEP_IDLE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CLK_COR_PRECEDENCE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CLK_COR_SEQ_LEN": {
        "type": "INT",
        "values": [1, 2, 3, 4],
        "encoding": [0, 1, 2, 3],
        "digits": 2
    },
    "CLK_COR_SEQ_2_2": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CLK_COR_SEQ_2_3": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "RXGEARBOX_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CLK_COR_SEQ_2_4": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_SEQ_1_ENABLE": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "CHAN_BOND_SEQ_1_1": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_SEQ_LEN": {
        "type": "INT",
        "values": [1, 2, 3, 4],
        "encoding": [0, 1, 2, 3],
        "digits": 2
    },
    "CHAN_BOND_SEQ_1_2": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_KEEP_ALIGN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CHAN_BOND_SEQ_1_3": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_SEQ_1_4": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_SEQ_2_ENABLE": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "CHAN_BOND_SEQ_2_USE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CHAN_BOND_SEQ_2_1": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "FTS_LANE_DESKEW_CFG": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "FTS_LANE_DESKEW_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "CHAN_BOND_SEQ_2_2": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "FTS_DESKEW_SEQ_ENABLE": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "CBCC_DATA_SOURCE_SEL": {
        "type": "STR",
        "values": ["ENCODED", "DECODED"],
        "digits": 1
    },
    "CHAN_BOND_SEQ_2_3": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "CHAN_BOND_MAX_SKEW": {
        "type": "INT",
        "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "encoding": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "digits": 4
    },
    "CHAN_BOND_SEQ_2_4": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "RXDLY_TAP_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "RXDLY_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "RXPH_MONITOR_SEL": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RX_DDI_SEL": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "TX_XCLK_SEL": {
        "type": "STR",
        "values": ["TXOUT", "TXUSR"],
        "digits": 1
    },
    "RXBUF_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TXOOB_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "LOOPBACK_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPI_CFG5": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TXPI_CFG4": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPI_CFG3": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPI_CFG2": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "TXPI_CFG1": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "TXPI_CFG0": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "SATA_PLL_CFG": {
        "type": "STR",
        "values": ["VCO_3000MHZ", "VCO_1500MHZ", "VCO_750MHZ"],
        "digits": 2
    },
    "TXPHDLY_CFG": {
        "type": "BIN",
        "values": [16711425],
        "digits": 24
    },
    "TXDLY_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "TXDLY_TAP_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "TXPH_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "TXPH_MONITOR_SEL": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RX_BIAS_CFG": {
        "type": "BIN",
        "values": [65535],
        "digits": 16
    },
    "RXOOB_CLK_CFG": {
        "type": "STR",
        "values": ["PMA", "FABRIC"],
        "digits": 1
    },
    "TX_CLKMUX_EN": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RX_CLKMUX_EN": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TERM_RCAL_CFG": {
        "type": "BIN",
        "values": [32767],
        "digits": 15
    },
    "TERM_RCAL_OVRD": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TX_CLK25_DIV": {
        "type":
        "INT",
        "values": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        ],
        "digits":
        5
    },
    "PMA_RSV5": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "PMA_RSV4": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "TX_DATA_WIDTH": {
        "type": "INT",
        "values": [16, 20, 32, 40],
        "encoding": [2, 3, 4, 5],
        "digits": 3
    },
    "PCS_RSVD_ATTR": {
        "type": "BIN",
        "values": [281462092005375],
        "digits": 48
    },
    "TX_MARGIN_FULL_1": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_FULL_0": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_FULL_3": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_FULL_2": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_LOW_0": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_FULL_4": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_LOW_2": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_LOW_1": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_LOW_4": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_MARGIN_LOW_3": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "TX_DEEMPH1": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "TX_DEEMPH0": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "TX_RXDETECT_REF": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TX_MAINCURSOR_SEL": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "PMA_RSV3": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "PMA_RSV7": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "PMA_RSV6": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TX_RXDETECT_CFG": {
        "type": "BIN",
        "values": [16383],
        "digits": 14
    },
    "CLK_COMMON_SWING": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RX_CM_TRIM": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "RXLPM_CFG1": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXLPM_CFG": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "PMA_RSV2": {
        "type": "BIN",
        "values": [4294836225],
        "digits": 32
    },
    "DMONITOR_CFG": {
        "type": "BIN",
        "values": [16711425],
        "digits": 24
    },
    "RXLPM_BIAS_STARTUP_DISABLE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXLPM_HF_CFG3": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "TXOUT_DIV": {
        "type": "INT",
        "values": [1, 2, 4, 8],
        "encoding": [0, 1, 2, 3],
        "digits": 3
    },
    "RXOUT_DIV": {
        "type": "INT",
        "values": [1, 2, 4, 8],
        "encoding": [0, 1, 2, 3],
        "digits": 3
    },
    "CFOK_CFG": {
        "type": "BIN",
        "values": [8791529752575],
        "digits": 43
    },
    "CFOK_CFG3": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "RXPI_CFG0": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "RXLPM_CM_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "CFOK_CFG5": {
        "type": "BIN",
        "values": [3],
        "digits": 2
    },
    "RXLPM_LF_CFG2": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXLPM_HF_CFG2": {
        "type": "BIN",
        "values": [31],
        "digits": 5
    },
    "RXLPM_IPCM_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXLPM_INCM_CFG": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "CFOK_CFG4": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "CFOK_CFG6": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "RXLPM_GC_CFG": {
        "type": "BIN",
        "values": [511],
        "digits": 9
    },
    "RXLPM_GC_CFG2": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "RXPI_CFG1": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXPI_CFG2": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXLPM_OSINT_CFG": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "ES_CLK_PHASE_SEL": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "USE_PCS_CLK_PHASE_SEL": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "CFOK_CFG2": {
        "type": "BIN",
        "values": [127],
        "digits": 7
    },
    "ADAPT_CFG0": {
        "type": "BIN",
        "values": [983025],
        "digits": 20
    },
    "TXPI_PPM_CFG": {
        "type": "BIN",
        "values": [255],
        "digits": 8
    },
    "TXPI_GREY_SEL": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPI_INVSTROBE_SEL": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "TXPI_PPMCLK_SEL": {
        "type": "STR",
        "values": ["TXUSRCLK", "TXUSRCLK2"],
        "digits": 1
    },
    "TXPI_SYNFREQ_PPM": {
        "type": "BIN",
        "values": [7],
        "digits": 3
    },
    "TST_RSV": {
        "type": "BIN",
        "values": [4294836225],
        "digits": 32
    },
    "PMA_RSV": {
        "type": "BIN",
        "values": [4294836225],
        "digits": 32
    },
    "RX_BUFFER_CFG": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "RXBUF_THRESH_OVRD": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXBUF_RESET_ON_EIDLE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXBUF_THRESH_UNDFLW": {
        "type":
        "INT",
        "values": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "RXBUF_EIDLE_HI_CNT": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "RXBUF_EIDLE_LO_CNT": {
        "type": "BIN",
        "values": [15],
        "digits": 4
    },
    "RXBUF_ADDR_MODE": {
        "type": "STR",
        "values": ["FULL", "FAST"],
        "digits": 1
    },
    "RXBUF_THRESH_OVFLW": {
        "type":
        "INT",
        "values": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "encoding": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63
        ],
        "digits":
        6
    },
    "RX_DEFER_RESET_BUF_EN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXBUF_RESET_ON_COMMAALIGN": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXBUF_RESET_ON_RATE_CHANGE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "RXBUF_RESET_ON_CB_CHANGE": {
        "type": "BOOL",
        "values": ["FALSE", "TRUE"],
        "digits": 1
    },
    "TXDLY_LCFG": {
        "type": "BIN",
        "values": [511],
        "digits": 9
    },
    "RXDLY_LCFG": {
        "type": "BIN",
        "values": [511],
        "digits": 9
    },
    "RXPH_CFG": {
        "type": "BIN",
        "values": [16711425],
        "digits": 24
    },
    "RXPHDLY_CFG": {
        "type": "BIN",
        "values": [16711425],
        "digits": 24
    },
    "RX_DEBUG_CFG": {
        "type": "BIN",
        "values": [16383],
        "digits": 14
    },
    "ES_PMA_CFG": {
        "type": "BIN",
        "values": [1023],
        "digits": 10
    },
    "RXCDR_PH_RESET_ON_EIDLE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXCDR_FR_RESET_ON_EIDLE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXCDR_HOLD_DURING_EIDLE": {
        "type": "BIN",
        "values": [1],
        "digits": 1
    },
    "RXCDR_LOCK_CFG": {
        "type": "BIN",
        "values": [63],
        "digits": 6
    },
    "RXCDR_CFG": {
        "type": "BIN",
        "values": [8461835120962772112965625],
        "digits": 83
    }
}

ports = {
    "inputs": [
        ("CFGRESET", 1),
        ("CLKRSVD0", 1),
        ("CLKRSVD1", 1),
        ("DMONFIFORESET", 1),
        ("DMONITORCLK", 1),
        ("DRPCLK", 1),
        ("DRPEN", 1),
        ("DRPWE", 1),
        ("EYESCANMODE", 1),
        ("EYESCANRESET", 1),
        ("EYESCANTRIGGER", 1),
        ("GTRESETSEL", 1),
        ("GTRXRESET", 1),
        ("GTTXRESET", 1),
        ("PMARSVDIN0", 1),
        ("PMARSVDIN1", 1),
        ("PMARSVDIN2", 1),
        ("PMARSVDIN3", 1),
        ("PMARSVDIN4", 1),
        ("RESETOVRD", 1),
        ("RX8B10BEN", 1),
        ("RXBUFRESET", 1),
        ("RXCDRFREQRESET", 1),
        ("RXCDRHOLD", 1),
        ("RXCDROVRDEN", 1),
        ("RXCDRRESET", 1),
        ("RXCDRRESETRSV", 1),
        ("RXCHBONDEN", 1),
        ("RXCHBONDMASTER", 1),
        ("RXCHBONDSLAVE", 1),
        ("RXCOMMADETEN", 1),
        ("RXDDIEN", 1),
        ("RXDFEXYDEN", 1),
        ("RXDLYBYPASS", 1),
        ("RXDLYEN", 1),
        ("RXDLYOVRDEN", 1),
        ("RXDLYSRESET", 1),
        ("RXGEARBOXSLIP", 1),
        ("RXLPMHFHOLD", 1),
        ("RXLPMHFOVRDEN", 1),
        ("RXLPMLFHOLD", 1),
        ("RXLPMLFOVRDEN", 1),
        ("RXLPMOSINTNTRLEN", 1),
        ("RXLPMRESET", 1),
        ("RXMCOMMAALIGNEN", 1),
        ("RXOOBRESET", 1),
        ("RXOSCALRESET", 1),
        ("RXOSHOLD", 1),
        ("RXOSINTEN", 1),
        ("RXOSINTHOLD", 1),
        ("RXOSINTNTRLEN", 1),
        ("RXOSINTOVRDEN", 1),
        ("RXOSINTPD", 1),
        ("RXOSINTSTROBE", 1),
        ("RXOSINTTESTOVRDEN", 1),
        ("RXOSOVRDEN", 1),
        ("RXPCOMMAALIGNEN", 1),
        ("RXPCSRESET", 1),
        ("RXPHALIGN", 1),
        ("RXPHALIGNEN", 1),
        ("RXPHDLYPD", 1),
        ("RXPHDLYRESET", 1),
        ("RXPHOVRDEN", 1),
        ("RXPMARESET", 1),
        ("RXPOLARITY", 1),
        ("RXPRBSCNTRESET", 1),
        ("RXRATEMODE", 1),
        ("RXSLIDE", 1),
        ("RXSYNCALLIN", 1),
        ("RXSYNCIN", 1),
        ("RXSYNCMODE", 1),
        ("RXUSERRDY", 1),
        ("RXUSRCLK2", 1),
        ("RXUSRCLK", 1),
        ("SETERRSTATUS", 1),
        ("SIGVALIDCLK", 1),
        ("TX8B10BEN", 1),
        ("TXCOMINIT", 1),
        ("TXCOMSAS", 1),
        ("TXCOMWAKE", 1),
        ("TXDEEMPH", 1),
        ("TXDETECTRX", 1),
        ("TXDIFFPD", 1),
        ("TXDLYBYPASS", 1),
        ("TXDLYEN", 1),
        ("TXDLYHOLD", 1),
        ("TXDLYOVRDEN", 1),
        ("TXDLYSRESET", 1),
        ("TXDLYUPDOWN", 1),
        ("TXELECIDLE", 1),
        ("TXINHIBIT", 1),
        ("TXPCSRESET", 1),
        ("TXPDELECIDLEMODE", 1),
        ("TXPHALIGN", 1),
        ("TXPHALIGNEN", 1),
        ("TXPHDLYPD", 1),
        ("TXPHDLYRESET", 1),
        ("TXPHDLYTSTCLK", 1),
        ("TXPHINIT", 1),
        ("TXPHOVRDEN", 1),
        ("TXPIPPMEN", 1),
        ("TXPIPPMOVRDEN", 1),
        ("TXPIPPMPD", 1),
        ("TXPIPPMSEL", 1),
        ("TXPISOPD", 1),
        ("TXPMARESET", 1),
        ("TXPOLARITY", 1),
        ("TXPOSTCURSORINV", 1),
        ("TXPRBSFORCEERR", 1),
        ("TXPRECURSORINV", 1),
        ("TXRATEMODE", 1),
        ("TXSTARTSEQ", 1),
        ("TXSWING", 1),
        ("TXSYNCALLIN", 1),
        ("TXSYNCIN", 1),
        ("TXSYNCMODE", 1),
        ("TXUSERRDY", 1),
        ("TXUSRCLK2", 1),
        ("TXUSRCLK", 1),
        ("RXADAPTSELTEST", 14),
        ("DRPDI", 16),
        ("GTRSVD", 16),
        ("PCSRSVDIN", 16),
        ("TSTIN", 20),
        ("RXELECIDLEMODE", 2),
        ("RXPD", 2),
        ("RXSYSCLKSEL", 2),
        ("TXPD", 2),
        ("TXSYSCLKSEL", 2),
        ("LOOPBACK", 3),
        ("RXCHBONDLEVEL", 3),
        ("RXOUTCLKSEL", 3),
        ("RXPRBSSEL", 3),
        ("RXRATE", 3),
        ("TXBUFDIFFCTRL", 3),
        ("TXHEADER", 3),
        ("TXMARGIN", 3),
        ("TXOUTCLKSEL", 3),
        ("TXPRBSSEL", 3),
        ("TXRATE", 3),
        ("TXDATA", 32),
        ("RXCHBONDI", 4),
        ("RXOSINTCFG", 4),
        ("RXOSINTID0", 4),
        ("TX8B10BBYPASS", 4),
        ("TXCHARDISPMODE", 4),
        ("TXCHARDISPVAL", 4),
        ("TXCHARISK", 4),
        ("TXDIFFCTRL", 4),
        ("TXPIPPMSTEPSIZE", 5),
        ("TXPOSTCURSOR", 5),
        ("TXPRECURSOR", 5),
        ("TXMAINCURSOR", 7),
        ("TXSEQUENCE", 7),
        ("DRPADDR", 9),
    ],
    "outputs": [
        ("DRPRDY", 1),
        ("EYESCANDATAERROR", 1),
        ("PHYSTATUS", 1),
        ("PMARSVDOUT0", 1),
        ("PMARSVDOUT1", 1),
        ("RXBYTEISALIGNED", 1),
        ("RXBYTEREALIGN", 1),
        ("RXCDRLOCK", 1),
        ("RXCHANBONDSEQ", 1),
        ("RXCHANISALIGNED", 1),
        ("RXCHANREALIGN", 1),
        ("RXCOMINITDET", 1),
        ("RXCOMMADET", 1),
        ("RXCOMSASDET", 1),
        ("RXCOMWAKEDET", 1),
        ("RXDLYSRESETDONE", 1),
        ("RXELECIDLE", 1),
        ("RXHEADERVALID", 1),
        ("RXOSINTDONE", 1),
        ("RXOSINTSTARTED", 1),
        ("RXOSINTSTROBEDONE", 1),
        ("RXOSINTSTROBESTARTED", 1),
        ("RXOUTCLK", 1),
        ("RXOUTCLKFABRIC", 1),
        ("RXOUTCLKPCS", 1),
        ("RXPHALIGNDONE", 1),
        ("RXPMARESETDONE", 1),
        ("RXPRBSERR", 1),
        ("RXRATEDONE", 1),
        ("RXRESETDONE", 1),
        ("RXSYNCDONE", 1),
        ("RXSYNCOUT", 1),
        ("RXVALID", 1),
        ("TXCOMFINISH", 1),
        ("TXDLYSRESETDONE", 1),
        ("TXGEARBOXREADY", 1),
        ("TXOUTCLK", 1),
        ("TXOUTCLKFABRIC", 1),
        ("TXOUTCLKPCS", 1),
        ("TXPHALIGNDONE", 1),
        ("TXPHINITDONE", 1),
        ("TXPMARESETDONE", 1),
        ("TXRATEDONE", 1),
        ("TXRESETDONE", 1),
        ("TXSYNCDONE", 1),
        ("TXSYNCOUT", 1),
        ("DMONITOROUT", 15),
        ("DRPDO", 16),
        ("PCSRSVDOUT", 2),
        ("RXCLKCORCNT", 2),
        ("RXDATAVALID", 2),
        ("RXSTARTOFSEQ", 2),
        ("TXBUFSTATUS", 2),
        ("RXBUFSTATUS", 3),
        ("RXHEADER", 3),
        ("RXSTATUS", 3),
        ("RXDATA", 32),
        ("RXCHARISCOMMA", 4),
        ("RXCHARISK", 4),
        ("RXCHBONDO", 4),
        ("RXDISPERR", 4),
        ("RXNOTINTABLE", 4),
        ("RXPHMONITOR", 5),
        ("RXPHSLIPMONITOR", 5),
    ],
}
