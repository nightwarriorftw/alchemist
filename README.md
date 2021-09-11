<p align="center">
    <img src="./public/logo.png" width="50px" height="50px"><br>
    <span style="font-family: cascadia-code; font-size: 18px;font-weight: bold;">Alchemist</span>
</p>

[![Open Issues](https://img.shields.io/github/issues/nightwarriorftw/alchemist?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/alchemist/issues) [![Forks](https://img.shields.io/github/forks/nightwarriorftw/alchemist?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/alchemist/network/members) [![Stars](https://img.shields.io/github/stars/nightwarriorftw/alchemist?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/alchemist/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2021?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarriorftw?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)

## :ledger: Index

- [:ledger: Index](#ledger-index)
- [:beginner: About](#beginner-about)
- [:zap: Features](#zap-features)
- [:wrench: Development](#wrench-development)
- [:star2: Credit/Acknowledgment](#star2-creditacknowledgment)
- [:lock: License](#lock-license)

## :beginner: About

Sometimes we want to restore deleted model instances but we don't have [Point in Time Recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html). So here comes **django-reversion** in the picture which allows version control over model instances. This projects is basically a demonstration of how to use django-reversion

Stay tuned for by blog post in case you want to understand how django-reversion works in deep :)

## :zap: Features

- restore deleted model instances
- simple admin integration

## :wrench: Development

The simplest way to use django-reversion is to register you models with a subclass `reversion.admin.VersionAdmin` .

- Simply install the django-reversion

```bash
pip install django-reversion
```

- Add `reversion` to `INSTALLED_APPS`

- Run `manage.py migrate`

The following template will give you a brief understanding of how you can use django-reversion in your admin panel.

```python

from django.contrib import admin
from full_metal.models import MarketingCampaign
from full_metal.models import Voucher

from reversion.admin import VersionAdmin


@admin.register(MarketingCampaign)
class MarketingCampaignAdmin(VersionAdmin):
    pass

```

## :star2: Credit/Acknowledgment

[Aman Verma](https://nightwarriorftw.netlify.app)

- Github: [nightwarriorftw](https://github.com/nightwarriorftw)
- Linkedin: [developer-aman-verma](https://linkedin.com/in/developer-aman-verma)
- Twitter: [nightwarriorftw](https://twitter.com/nightwarriorftw)

## :lock: License

[LICENSE](/LICENSE)
