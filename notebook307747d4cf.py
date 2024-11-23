{
  "metadata": {
    "kernelspec": {
      "language": "python",
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.14",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kaggle": {
      "accelerator": "none",
      "dataSources": [
        {
          "sourceId": 9991801,
          "sourceType": "datasetVersion",
          "datasetId": 6149456
        },
        {
          "sourceId": 9992380,
          "sourceType": "datasetVersion",
          "datasetId": 6149857
        },
        {
          "sourceId": 9992518,
          "sourceType": "datasetVersion",
          "datasetId": 6149939
        }
      ],
      "dockerImageVersionId": 30786,
      "isInternetEnabled": false,
      "language": "python",
      "sourceType": "notebook",
      "isGpuEnabled": false
    },
    "colab": {
      "name": "notebook307747d4cf",
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ZJIou/11111/blob/main/notebook307747d4cf.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from PIL import Image"
      ],
      "metadata": {
        "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
        "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2024-11-23T15:25:15.162195Z",
          "iopub.execute_input": "2024-11-23T15:25:15.162566Z",
          "iopub.status.idle": "2024-11-23T15:25:15.706867Z",
          "shell.execute_reply.started": "2024-11-23T15:25:15.162535Z",
          "shell.execute_reply": "2024-11-23T15:25:15.705611Z"
        },
        "id": "qOUFJjsSwgST"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "img_fns = Image.open('/kaggle/input/111112222/11112222/e0186c1c62818654.jpg')"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2024-11-23T15:28:37.059211Z",
          "iopub.execute_input": "2024-11-23T15:28:37.059617Z",
          "iopub.status.idle": "2024-11-23T15:28:37.066322Z",
          "shell.execute_reply.started": "2024-11-23T15:28:37.059583Z",
          "shell.execute_reply": "2024-11-23T15:28:37.06502Z"
        },
        "id": "ilHBWWDTwgSU"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "import easyocr\n",
        "\n",
        "reader = easyocr.Reader(['en'], gpu = False)\n"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2024-11-23T15:35:13.479568Z",
          "iopub.execute_input": "2024-11-23T15:35:13.480022Z",
          "iopub.status.idle": "2024-11-23T15:35:22.015932Z",
          "shell.execute_reply.started": "2024-11-23T15:35:13.479976Z",
          "shell.execute_reply": "2024-11-23T15:35:22.014963Z"
        },
        "id": "zlW-Pa4NwgSX"
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": [
        "results = reader.readtext(\"/kaggle/input/111112222/11112222/e116b3dd0085f2e2.jpg\",detail=0,paragraph=True)\n",
        "print(results)"
      ],
      "metadata": {
        "trusted": true,
        "execution": {
          "iopub.status.busy": "2024-11-23T15:36:54.643724Z",
          "iopub.execute_input": "2024-11-23T15:36:54.644123Z",
          "iopub.status.idle": "2024-11-23T15:37:03.790613Z",
          "shell.execute_reply.started": "2024-11-23T15:36:54.644086Z",
          "shell.execute_reply": "2024-11-23T15:37:03.789012Z"
        },
        "id": "ZH2EpjhHwgSY",
        "outputId": "ce289923-7242-405d-cdb0-1987b26fe567"
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "[\"LINDEMANS 21N 40 MERLOT respected and endurie Lindemans is one of the most wines since 1843 Australian winemakers, crafting Bin Seta to the next; Lindemans Consistent from one year range of ' MTIA has become one of the worlds favourite cipe: full Lindemans Bin 40 Merlot is smooch; enjoyed with flavoured wine that can be Italian and red meat dishes: AusTRalIa Tlnle SouTHvEAsTeRN AUSTRALIA AQAD; KARAdOC Maoouced AND BoTtled BY LINOEMANS WINES, Edey MiERU staEET ~ MWICAEMHAM Wptated 8y UndeMANS Wines, 15 Chuach MT\"]\n",
          "output_type": "stream"
        }
      ],
      "execution_count": null
    }
  ]
}