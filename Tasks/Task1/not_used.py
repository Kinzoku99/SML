def make_quadratic_histograms(data, a=3):
    dist_range = np.arange(a, dtype=np.uint8)
    distributions = ps.make_subplots(subplot_titles=data.columns, rows=a, cols=a)
    for i, col in enumerate(data.columns):
        histogram = px.histogram(data, x=col, title=col)
        mu, std = np.mean(data[col]), np.std(data[col])
        m, M = np.min(data[col]), np.max(data[col])
        y_vals = norm.pdf(np.linspace(mu-3*std, mu+3*std), loc=mu, scale=std)
        # print(len(data[col]), histogram['data'][0]['xbins'].size )
        y_vals *= 50 * (np.max(data[col]) - np.min(data[col]))
        histogram.add_trace(
            go.Scatter(x=np.linspace(mu-3*std, mu+3*std), y=y_vals,
            name='Gaussian')
        )
        # histogram.show()
        distributions.add_trace(histogram['data'][0], row=(i % 3) + 1, col=(i // 3) + 1)
        x_range = [min(data[col]), max(data[col])]
        y_range = [0, max(y_vals) * 1.1]  # Adjust the y-axis range as needed
        distributions.update_xaxes(range=x_range, row=(i % 3) + 1, col=(i // 3) + 1)
        distributions.update_yaxes(range=y_range, row=(i % 3) + 1, col=(i // 3) + 1)
    distributions.update_layout(height=800, width=800, title_text="Distributions")
    return distributions

make_quadratic_histograms(quantitative_data)