/**
 * Crypto Price Prediction Dashboard
 * Fetches data from the Flask API and renders interactive Plotly charts.
 */

class Dashboard {
    constructor() {
        this.priceChart = null;
        this.predictionChart = null;
        this.refreshInterval = 60000; // 60 seconds
        this.initialize();
    }

    initialize() {
        this.fetchPredictions();
        this.fetchPerformance();
        this.startAutoRefresh();
    }

    /**
     * Fetch latest prediction data from the API and update UI.
     */
    async fetchPredictions() {
        try {
            const response = await fetch('/api/v1/predictions?symbol=BTC/USDT');
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();

            // Update stat cards
            document.getElementById('current-price').textContent =
                `$${parseFloat(data.current_price).toLocaleString('en-US', {minimumFractionDigits: 2})}`;
            document.getElementById('predicted-price').textContent =
                `$${parseFloat(data.predicted_price).toLocaleString('en-US', {minimumFractionDigits: 2})}`;

            const directionEl = document.getElementById('direction');
            directionEl.textContent = data.direction === 'up' ? '▲ Up' : '▼ Down';
            directionEl.style.color = data.direction === 'up' ? '#00e676' : '#ff5252';

            const confEl = document.getElementById('confidence');
            confEl.textContent = `${(data.prediction_probability * 100).toFixed(1)}%`;
        } catch (err) {
            console.error('Failed to fetch predictions:', err);
        }
    }

    /**
     * Fetch performance metrics and render charts / metric cards.
     */
    async fetchPerformance() {
        try {
            const response = await fetch('/api/v1/performance');
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();

            this.renderMetrics(data);
            this.createCharts(data);
        } catch (err) {
            console.error('Failed to fetch performance:', err);
            document.getElementById('metrics-content').textContent =
                'Unable to load metrics. Start the prediction pipeline first.';
        }
    }

    /**
     * Render performance metrics into the DOM.
     */
    renderMetrics(data) {
        const container = document.getElementById('metrics-content');
        const metrics = [
            { label: 'Win Rate', value: `${(data.accuracy * 100).toFixed(1)}%`, positive: data.accuracy > 0.5 },
            { label: 'Profit / Loss', value: `${data.profit_loss > 0 ? '+' : ''}${data.profit_loss.toFixed(2)}%`, positive: data.profit_loss > 0 },
            { label: 'Sharpe Ratio', value: data.sharpe_ratio.toFixed(3), positive: data.sharpe_ratio > 1 },
            { label: 'Max Drawdown', value: `${(data.max_drawdown * 100).toFixed(2)}%`, positive: false },
            { label: 'Total Trades', value: data.total_trades, positive: true },
        ];

        container.innerHTML = metrics.map(m => `
            <div class="metric-item">
                <span class="label">${m.label}</span>
                <span class="value ${m.positive ? 'positive' : 'negative'}">${m.value}</span>
            </div>
        `).join('');
    }

    /**
     * Create Plotly charts for price history and portfolio performance.
     */
    createCharts(performanceData) {
        const darkLayout = {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#a0a0b0', family: 'Inter, sans-serif', size: 12 },
            margin: { l: 50, r: 20, t: 10, b: 40 },
            xaxis: {
                gridcolor: 'rgba(255,255,255,0.04)',
                zerolinecolor: 'rgba(255,255,255,0.06)',
            },
            yaxis: {
                gridcolor: 'rgba(255,255,255,0.04)',
                zerolinecolor: 'rgba(255,255,255,0.06)',
            },
        };

        // Price chart placeholder (actual data would come from a more detailed API)
        const priceTrace = {
            y: Array.from({ length: 60 }, (_, i) => 45000 + Math.sin(i / 5) * 2000 + Math.random() * 500),
            type: 'scatter',
            mode: 'lines',
            name: 'BTC/USDT',
            line: { color: '#448aff', width: 2 },
            fill: 'tozeroy',
            fillcolor: 'rgba(68, 138, 255, 0.08)',
        };

        Plotly.newPlot('price-chart', [priceTrace], {
            ...darkLayout,
            yaxis: { ...darkLayout.yaxis, title: 'Price (USDT)' },
        }, { responsive: true, displayModeBar: false });

        // Portfolio performance gauge
        const gaugeTrace = {
            type: 'indicator',
            mode: 'gauge+number+delta',
            value: performanceData.profit_loss,
            delta: { reference: 0, increasing: { color: '#00e676' }, decreasing: { color: '#ff5252' } },
            gauge: {
                axis: { range: [-50, 50], tickcolor: '#a0a0b0' },
                bar: { color: performanceData.profit_loss >= 0 ? '#00e676' : '#ff5252' },
                bgcolor: 'rgba(0,0,0,0)',
                bordercolor: 'rgba(255,255,255,0.06)',
                steps: [
                    { range: [-50, 0], color: 'rgba(255, 82, 82, 0.1)' },
                    { range: [0, 50], color: 'rgba(0, 230, 118, 0.1)' },
                ],
            },
            number: { suffix: '%', font: { color: '#e0e0e0', size: 28 } },
        };

        Plotly.newPlot('probability-gauge', [gaugeTrace], {
            ...darkLayout,
            margin: { l: 30, r: 30, t: 30, b: 10 },
            height: 250,
        }, { responsive: true, displayModeBar: false });
    }

    /**
     * Auto-refresh predictions every 60 seconds.
     */
    startAutoRefresh() {
        setInterval(() => {
            this.fetchPredictions();
        }, this.refreshInterval);
    }
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new Dashboard();
});