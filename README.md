# GreatHR Automation Tool 🤖

An automated attendance logging system for GreatHR that handles sign-in/sign-out operations for multiple users with scheduled execution.

## ✨ Features

- **Automated Attendance**: Automatically logs into GreatHR and performs sign-in/sign-out operations
- **Multi-user Support**: Handles multiple user accounts from a single configuration
-- **Scheduled Execution**: Runs automatically at user-defined times on weekdays
- **Error Handling**: Robust error handling with retry mechanisms
- **Notification Support**: Webhook integration for status notifications
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Chrome browser installed
- Chrome WebDriver (automatically managed by Selenium 4.x)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/mubashirm1/automate_greathr.git
cd automate_greathr
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment files:

Create `.env.secret` with your credentials:

```env
USER1_USERNAME=your_username1
USER1_PASSWORD=your_password1
USER2_USERNAME=your_username2
USER2_PASSWORD=your_password2
```

Create `.env.shared` for notifications (optional):

```env
WEBHOOK=your_webhook_url
```

### Usage

#### Manual Execution

Run the main automation script:

```python
from main import main
main()
```

#### Scheduled Execution

Start the scheduler for automatic execution:

```bash
python scheduler.py
```

The scheduler will run the automation at the times you configure in `scheduler.py`.

## 📁 Project Structure

```text
automate_greathr/
├── main.ipynb          # Main automation logic (Jupyter notebook)
├── module.ipynb        # Core functions and utilities (Jupyter notebook)
├── scheduler.py        # Scheduling configuration
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .env.secret        # User credentials (not tracked)
└── .env.shared        # Shared configuration (not tracked)
```

## 🔧 Configuration

### User Credentials

Add users to `.env.secret` following this pattern:

```env
USERNAME_USERNAME=actual_username
USERNAME_PASSWORD=actual_password
```

Where `USERNAME` is a unique identifier for each user.

### Scheduling

Modify `scheduler.py` to set your preferred execution times. See APScheduler documentation for details.

### Notification Webhook

Set up webhook notifications in `.env.shared`:

```env
WEBHOOK=https://your-webhook-url.com
```

## 🛠️ Core Functions

### `greathr_logger(driver, username, password)`

- Handles the complete login and attendance marking process
- Navigates shadow DOM elements for button interactions
- Includes proper wait times and error handling

### `fetching_credentials(secret_path)`

- Parses credentials from environment files
- Returns structured dictionary for multi-user support

### `main()`

- Orchestrates the entire automation process
- Manages WebDriver instances and cleanup
- Implements retry logic for failed attempts

## ⚙️ How It Works

1. **Credential Loading**: Reads user credentials from `.env.secret`
2. **Browser Automation**: Uses Selenium to navigate the GreatHR portal
3. **Login Process**: Automatically fills credentials and logs in
4. **Attendance Marking**: Finds and clicks the sign-in/sign-out button
5. **Cleanup**: Properly closes browser instances
6. **Retry Logic**: Attempts up to 3 times per user if failures occur

## 🔒 Security Notes

- **Never commit** `.env.secret` or `.env.shared` files to version control
- Store sensitive credentials securely
- Use environment variables in production environments
- Consider using encrypted credential storage for enhanced security

## 🐛 Troubleshooting

### Common Issues

1. **Chrome Driver Issues**
   - Ensure Chrome browser is installed and updated
   - Selenium 4.x automatically manages WebDriver

2. **Login Failures**
   - Verify credentials in `.env.secret`
   - Check if GreatHR portal is accessible
   - Ensure proper network connectivity

3. **Element Not Found**
   - Website structure might have changed
   - Check if shadow DOM elements are still valid
   - Update selectors in `greathr_logger` function

4. **Scheduling Issues**
   - Verify your timezone settings
   - Check system time and date
   - Ensure Python process has necessary permissions

## 📊 Dependencies

Key dependencies include:

- `selenium`: Web automation
- `APScheduler`: Task scheduling
- `python-dotenv`: Environment variable management
- `import-ipynb`: Jupyter notebook imports
- `pytz`: Timezone handling

See `requirements.txt` for the complete list.

## 🚦 Running in Production

For production deployment:

1. **Use a process manager** like `pm2` or `systemd`
2. **Set up logging** for monitoring and debugging
3. **Configure proper error notifications**
4. **Use secure credential management**
5. **Monitor system resources**

Example with pm2:

```bash
pm2 start scheduler.py --name "greathr-automation"
pm2 save
pm2 startup
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Create Pull Request

## ⚠️ Disclaimer

This tool is for educational and personal use only. Ensure compliance with your organization's policies regarding automated systems. Use responsibly and at your own risk.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For questions or issues:

- Open an issue on GitHub

---

**Note**: This automation tool is designed for the GreatHR portal. Modifications may be needed for other GreatHR instances.