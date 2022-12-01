# Tools

## GitHub

* [how to](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) use a branch
* [how to](https://docs.github.com/en/get-started/using-git/about-git) pull, commit and push a change
* what the [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) is

## IDE

### Prerequisites

* [Visual Studio Code](https://code.visualstudio.com/) (VS Code)
* [Extensions](https://code.visualstudio.com/docs/datascience/data-science-tutorial) for VS Code

### Environment

The best practice is to use a virtual environment where you can install all necessary without dirty your computer. And after you can associate this environment to your Jupyter Notebook when you select the [kernel](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook).

```sh
pip3 install virtualenv
virtualenv .env # to create environment
source .env/bin/activate # to enter into your environment on the terminal 
ipython kernel install --user --name=my_jupyter_kernel # to associate your environment with the name my_jupyter_kernel that you have to use on VS Code like your Jupyter Kernel
```

## Python packages

The method to install on your environment the Python packages, when they are a lots, it is by a file that you can find in the document root of thie repository.

```sh
pip3 install -r requirements.txt
```

Some of packages that we are going to learn.

* [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/), [scipy](https://pypi.org/project/scipy/) and [matplotlib](https://pypi.org/project/matplotlib/)
* [picamera](https://pypi.org/project/picamera/) or [picamera2](https://pypi.org/project/picamera2/)
* [opencv-python](https://pypi.org/project/opencv-python/) and [yolo](https://pypi.org/project/yolov5/)
