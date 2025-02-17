# -*- coding: utf-8 -*-
import os
from cms.envs.devstack import *

LMS_BASE = "{{ LMS_HOST }}:8000"
LMS_ROOT_URL = "http://" + LMS_BASE
FEATURES["PREVIEW_LMS_BASE"] = "{{ PREVIEW_LMS_HOST }}:8000"

{% include "apps/openedx/settings/partials/common_cms.py" %}

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

{{ patch("openedx-development-settings") }}
{{ patch("openedx-cms-development-settings") }}
