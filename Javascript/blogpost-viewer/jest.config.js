module.exports = {
  transform: {
    '^.+\\.[jt]sx?$': ['babel-jest', { configFile: './babel.config.jest.js' }],
  },
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    '\\.(css|scss|sass)$': 'identity-obj-proxy',
    '^@/(.*)$': '<rootDir>/$1',
  },
  
};