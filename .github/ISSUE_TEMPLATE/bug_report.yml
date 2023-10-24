name: "🔍 Bug Report"
description: "📝 Report a bug or issue related to the content or code."
title: "🐍 [BUG] - <title>"
labels: 
  - "bug"
body:
  - type: textarea
    id: description
    attributes:
      label: "📖 Description"
      description: "🖋️ Please provide a detailed description of the issue or bug."
      placeholder: "🤔 Describe the issue you encountered..."
    validations:
      required: true
  - type: textarea
    id: reprod
    attributes:
      label: "🔁 Reproduction steps"
      description: "👣 Please describe the steps to reproduce the issue, especially if it's related to code or content errors."
      value: |
        1. 📄 Open file '...'
        2. ⌨️ Run the command '....'
        3. ❗ See error message '....'
    validations:
      required: true
  - type: textarea
    id: screenshot
    attributes:
      label: "🖼️ Screenshots or Error Logs"
      description: "📸 If applicable, add screenshots or paste the error logs to help explain the issue. If adding an image, upload it to an image hosting service and provide the link here."
      value: |
        ![DESCRIPTION](LINK.png)
    validations:
      required: false
  - type: dropdown
    id: python-version
    attributes:
      label: "🐍 Python Version"
      description: "🔢 Which version of Python are you using when you encountered the issue?"
      options:
        - Python 2.7
        - Python 3.6
        - Python 3.7
        - Python 3.8
        - Python 3.9
        - Python 3.10
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: "💻 Operating System"
      description: "🌐 On which operating system did you encounter this issue?"
      options:
        - Windows
        - Linux
        - Mac
    validations:
      required: true
