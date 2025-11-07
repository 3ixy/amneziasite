import React, {type ReactNode} from 'react';
import Layout from '@theme-original/Layout';
import type LayoutType from '@theme/Layout';
import type {WrapperProps} from '@docusaurus/types';

type Props = WrapperProps<typeof LayoutType>;

export default function LayoutWrapper(props: Props): ReactNode {
  return (
    <>
          <Layout {...props}>
      <a
        style={{
          background: '#0F0F0F',
          color: '#fff',
          padding: '10px 0',
          textAlign: 'center',
          fontSize: '0.95rem',
          display: 'block',
        }}
        href='https://xorek.cloud/?ref=18'
      >
        <img src='https://amnezia-vpn.site/white-logo.png' height='50PX'></img><br />
        <b>Мгновенный запуск - VPS сервер готов через 2 минуты!</b>
      </a>
      {props.children}
    </Layout>
    </>
  );
}
