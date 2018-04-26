# A/B Testing

**WORK IN PROGRESS WARNING!**

If you have questions, ideas, comments then I would love to hear from you!
You can either use the issues or send me an email drorata@gmail.com.

Thanks!

## The notebooks

The notebooks in this repository can be accessed using one of two methods:

### Binderhub

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/drorata/abtest/master?filepath=%2Fnotebooks)

This will run a remote environment where you can play around interactively with the notebooks

### (Local) docker

A `Dockerfile` is provided as well.
To use it, simply build it:

```bash
$ docker build -t abtest .
```

Make sure you execute the above from the root directory of the repository.
Furthermore, `abtest` is the name of the image to be built; you can change it as you wish.
Secondly, run the image:

```bash
$ docker run -it --rm -p 8811:8888 abtest
```

This way, the Jupyter server which will start in the container will be accessible at `localhost:8811`.

## Credits

This package was created with [`Cookiecutter`](https://github.com/audreyr/cookiecutter) and the [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.
