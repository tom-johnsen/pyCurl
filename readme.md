# pyCurl - Simple HTTP Client

pyCurl is a simple command-line HTTP client built using Python. It allows you to make HTTP requests to any given URL and provides information such as response status code, headers, and body.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

```shell
./pyCurl.py [-h] [-U USER_AGENT] [-R] url
```

- `-U, --user-agent`: Specify the User-Agent header for the request.
- `-R, --redirect`: Follow redirects automatically.
- `url`: The URL to make the HTTP request to.

## Example

To make a request to a specific URL:

```shell
./pyCurl.py https://example.com
```

To specify a custom User-Agent header:

```shell
./pyCurl.py -U "My Custom User-Agent" https://example.com
```

To follow redirects:

```shell
./pyCurl.py -R https://example.com
```

## Output

The output of the script includes the following information:

- **Status code**: The HTTP status code of the response.
- **Headers**: The response headers.
- **Body**: The body of the response.

## Default User-Agent

If no User-Agent is specified, pyCurl uses the default value `pyCurl/1.0` as the User-Agent header.

## URL Format

The script automatically adds the `http://` prefix if the URL doesn't start with `http://` or `https://`.

## Error Handling

If there is no response or an error occurs during the request, the script will display a "No Response" message.

## License

This project is licensed under the [MIT License](LICENSE).
