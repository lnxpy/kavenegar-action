## Kavenegar Action

<img alt="action-badge" src="https://img.shields.io/badge/Kavenegar Action-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> <a href="https://github.com/lnxpy/pyaction"><img alt="pyaction" src="https://img.shields.io/badge/PyAction-white?&label=Made%20with&labelColor=white&color=0064D7"></a>

Send SMS within your workflows.

### Usage
You can use this action to send messages about the events happening to your repository. In this example, whenever someone opens a new issue on the repository, there will be an SMS sent to your phone.

```yml
name: Issue-opening Notifier
on:
  issues:
    types: [opened]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Sending SMS
        uses: lnxpy/kavenegar_action@v1
        with:
          api_key: ${{ secrets.API_KEY }}
          receptor: ${{ secrets.RECEPTOR }}
          message: ${{ github.event.issue.title }} is opened on your repository!
```

Keep in mind to set the `secrets`. Here is a [quick guide](https://docs.github.com/en/actions/security-guides/encrypted-secrets) about it. Generate `API_KEY` from your profile dashboard on [Kavenegar](https://kavenegar.com/).

### License
This action is licensed under some specific terms. Check [here](LICENSE) for more information.